import numpy as np
from scipy.optimize import least_squares

from catrxneng.quantities import *


class KineticModel:

    def __init__(self, limiting_reactant, T):
        self.limiting_reactant = limiting_reactant
        self.fugacity_coeff = np.ones(len(self.components))
        self.std_state_fugacity = std_state_fugacity.bar
        self.T = T
        if self.T is not None:
            self.compute_temp_dependent_constants()

    def compute_temp_dependent_constants(self):
        pass

    def _compute_final_molfrac(self, initial_moles, extent):
        delta_moles = self.stoich_coeff.T @ extent
        final_moles = initial_moles + delta_moles
        total_final_moles = np.sum(final_moles)
        molfrac = final_moles / total_final_moles
        return molfrac, delta_moles

    def _compute_extent_bounds(self, initial_moles):
        lower_bounds = [0] * len(self.reactions)
        upper_bounds = []
        for i in range(len(self.reactions)):
            stoich_lim = self.stoich_coeff[i][self.comp_idx[self.limiting_reactant]]
            max_extent = initial_moles[self.comp_idx[self.limiting_reactant]] / abs(
                stoich_lim
            )
            upper_bounds.append(max_extent)
        return (lower_bounds, upper_bounds)

    def _equilibrium_objective(self, extent, P, initial_moles, Keq):
        molfrac = self._compute_final_molfrac(initial_moles, extent)[0]
        molfrac[molfrac < 0] = 0.00001
        p = molfrac * P
        fugacity = self.fugacity_coeff * p
        activity = fugacity / self.std_state_fugacity
        K_calc = np.prod(activity**self.stoich_coeff, axis=1)
        return (np.log(K_calc) - np.log(Keq)) ** 2

    def equilibrate(self, p0, T, initial_guesses=None, allow_component_mismatch=False):
        if T and T != self.T:
            self.T = T
            self.compute_temp_dependent_constants()
        initial_total_moles = 100
        if allow_component_mismatch:
            p0_bar = [p0[comp].bar for comp in self.components]
            p0 = Pressure(bar=p0_bar, keys=self.components)
        P = np.sum(p0)
        initial_molfrac = p0 / P
        initial_moles = (initial_molfrac * initial_total_moles).si
        if not initial_guesses:
            num_rxns = len(self.reactions)
            initial_guess = (
                initial_moles[self.comp_idx[self.limiting_reactant]] / num_rxns
            )
            initial_guesses = np.ones(num_rxns) * initial_guess / 2

        def objective(extent):
            return self._equilibrium_objective(extent, P.bar, initial_moles, self.Keq)

        solution = least_squares(
            objective,
            initial_guesses,
            bounds=self._compute_extent_bounds(initial_moles),
            method="trf",
            ftol=1e-10,
            max_nfev=1000,
        )
        extent = solution.x
        eq_molfrac, delta_moles = self._compute_final_molfrac(initial_moles, extent)
        delta = delta_moles[self.comp_idx[self.limiting_reactant]]
        initial = initial_moles[self.comp_idx[self.limiting_reactant]]
        self.eq_conversion = Unitless(si=-delta / initial)
        self.eq_molfrac = Unitless(si=eq_molfrac, keys=self.components)

    def carbon_balance(self, reactor):
        carbon_in = np.sum(reactor.F0 * self.carbon_atoms)
        carbon_out = np.sum(reactor.F * self.carbon_atoms[:, np.newaxis], axis=0)
        return carbon_out / carbon_in
