import numpy as np
from scipy.optimize import minimize

from catrxneng.quantities import *


class Reaction:
    def __init__(self, T, limiting_reactant):
        self.limiting_reactant = limiting_reactant
        self.T = T
        self.fug_coeff = Unitless(
            si=np.ones(len(self.components)), keys=list(self.components.keys())
        )
        # self.update()

    @property
    def active_components(self):
        return {key: self.components[key] for key in self.components if key != "inert"}

    @property
    def stoich_coeff_active(self):
        return Unitless(
            si=self.stoich_coeff.si[self.stoich_coeff.si != 0],
            keys=list(self.active_components.keys()),
        )

    @property
    def dH_rxn_298_gas(self):
        Hf_298_gas = np.array(
            [self.components[key].Hf_298_gas.si for key in self.active_components]
        )
        dHr_298_gas = np.sum(Hf_298_gas * self.stoich_coeff_active.si)
        return Energy(si=dHr_298_gas)

    def dH_rxn_gas(self, T=None):
        if not T:
            T = self.T
        Hf_gas = np.array(
            [self.components[key].Hf_gas(T).si for key in self.active_components]
        )
        dHr_gas = np.sum(Hf_gas * self.stoich_coeff_active.si)
        return Energy(si=dHr_gas)

    @property
    def dS_rxn_298_gas(self):
        S_298_gas = np.array(
            [self.components[key].S_298_gas.si for key in self.active_components]
        )
        dSr_298_gas = np.sum(S_298_gas * self.stoich_coeff_active.si)
        return Entropy(si=dSr_298_gas)

    def dS_rxn_gas(self, T=None):
        if not T:
            T = self.T
        Sf_gas = np.array(
            [self.components[key].Sf_gas(T).si for key in self.active_components]
        )
        dSr_gas = np.sum(Sf_gas * self.stoich_coeff_active.si)
        return Energy(si=dSr_gas)

    @property
    def dG_rxn_298_gas(self):
        T = Temperature(K=298)
        return self.dH_rxn_298_gas - T * self.dS_rxn_298_gas

    def dG_rxn(self, T=None):
        if not T:
            T = self.T
        return self.dH_rxn(T) - T * self.dS_rxn(T)

    def dG_rxn_gas(self, T=None):
        if not T:
            T = self.T
        return self.dH_rxn_gas(T) - T * self.dS_rxn_gas(T)

    def Keq(self, T=None):
        if not T:
            T = self.T
        return np.exp(-self.dG_rxn(T) / (R * T)).si

    def check_components(self, p0, allow_component_mismatch):
        if p0.keys != list(self.components.keys()) and not allow_component_mismatch:
            raise ValueError("Partial pressure keys do not match reaction components.")

    def equilibrate(self, p0, T, allow_component_mismatch=False):
        self.check_components(p0,allow_component_mismatch=allow_component_mismatch)
        if allow_component_mismatch:
            p0_bar = [p0[comp].bar for comp in list(self.components.keys())]
            p0 = Pressure(bar=p0_bar, keys=list(self.components.keys()))
        P = np.sum(p0)
        initial_total_moles = Moles(si=100)
        initial_molfrac = p0 / P
        initial_moles = initial_molfrac * initial_total_moles
        std_state_fugacity = Pressure(atm=np.ones(len(self.components)))

        def objective(extent):
            extent = Moles(si=extent)
            moles = initial_moles + extent * self.stoich_coeff
            total_moles = np.sum(moles)
            molfrac = moles / total_moles
            fugacity = molfrac * self.fug_coeff * P
            activity = fugacity / std_state_fugacity
            Ka = np.prod(activity**self.stoich_coeff)
            # Kx = np.prod(molfrac**self.stoich_coeff)
            # Kphi = np.prod(self.fug_coeff**self.stoich_coeff)
            # Kp = np.prod(P**self.stoich_coeff)
            # Kf0 = np.prod(std_state_fugacity**self.stoich_coeff)
            return ((Ka - self.Keq(T)) ** 2).si * 1e5

        adj_init_mol_reactants = np.array(
            [
                mol / stoich_coeff
                for mol, stoich_coeff in zip(initial_moles.si, self.stoich_coeff.si)
                if stoich_coeff < 0
            ]
        )
        min_extent = 1e-5
        bounds = [(min_extent, np.min(-adj_init_mol_reactants) * (1 - min_extent))]
        initial_guess = -0.5 * initial_moles.si[0] / self.stoich_coeff.si[0]
        result = minimize(
            objective,
            initial_guess,
            bounds=bounds,
            options={"ftol": 1e-10},
        )
        if result.success:
            self.extent = Moles(si=result.x[0])
            moles = initial_moles + self.extent * self.stoich_coeff
            self.eq_conversion = (
                initial_moles[self.limiting_reactant] - moles[self.limiting_reactant]
            ) / initial_moles[self.limiting_reactant]
            total_moles = Moles(si=np.sum(moles.si))
            self.eq_molfrac = moles / total_moles
        else:
            raise ValueError("Optimization failed: " + result.message)
