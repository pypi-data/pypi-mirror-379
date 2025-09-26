import scipy.integrate as integrate

from .reaction import Reaction
from ..quantities import *
from ..species import *


class RWGS(Reaction):
    def __init__(self, T=None, limiting_reactant="co2"):
        self.components = {
            "co2": CO2(T=T),
            "h2": H2(T=T),
            "co": CO(T=T),
            "h2o": H2O(T=T),
            "inert": Ar(T=T),
        }
        self.stoich_coeff = Unitless(
            si=[-1.0, -1.0, 1.0, 1.0, 0.0], keys=list(self.components.keys())
        )
        super().__init__(T=T, limiting_reactant=limiting_reactant)

    def dCp_1(self, T_K):
        T = Temperature(K=T_K)
        dCp = CO().Cp_gas(T) + H2O().Cp_liq(T) - CO2().Cp_gas(T) - H2().Cp_gas(T)
        return dCp.JmolK

    def dCp_2(self, T_K):
        T = Temperature(K=T_K)
        dCp = CO().Cp_gas(T) + H2O().Cp_gas(T) - CO2().Cp_gas(T) - H2().Cp_gas(T)
        return dCp.JmolK

    @property
    def dH_rxn_298(self):
        return CO().HF_298_GAS + H2O().HF_298_LIQ - CO2().HF_298_GAS - H2().HF_298_GAS

    @property
    def dH_rxn_298_gas(self):
        return CO().HF_298_GAS + H2O().HF_298_GAS - CO2().HF_298_GAS - H2().HF_298_GAS

    @property
    def dS_rxn_298(self):
        return CO().S_298_GAS + H2O().S_298_LIQ - CO2().S_298_GAS - H2().S_298_GAS

    def dH_rxn(self, T=None):
        Tb_h2o = H2O().BOILING_TEMP.K
        if T.K < Tb_h2o:
            dHr = self.dH_rxn_298.Jmol
            dHr += integrate.quad(self.dCp_1, 298, T.K)[0]
            return Energy(Jmol=dHr)
        if T.K >= Tb_h2o:
            dHr = self.dH_rxn_298.Jmol
            dHr += integrate.quad(self.dCp_1, 298, Tb_h2o)[0]
            dHr += H2O().DH_VAP.Jmol
            dHr += integrate.quad(self.dCp_2, Tb_h2o, T.K)[0]
            return Energy(Jmol=dHr)

    def dS_rxn(self, T=None):
        Tb_h2o = H2O().BOILING_TEMP.K
        integrand1 = lambda T_K: self.dCp_1(T_K) / T_K
        integrand2 = lambda T_K: self.dCp_2(T_K) / T_K
        if T.K < Tb_h2o:
            dSr = self.dS_rxn_298.JmolK
            dSr += integrate.quad(integrand1, 298, T.K)[0]
            return Entropy(JmolK=dSr)
        if T.K >= Tb_h2o:
            dSr = self.dS_rxn_298.JmolK
            dSr += integrate.quad(integrand1, 298, Tb_h2o)[0]
            dSr += H2O().DS_VAP.JmolK
            dSr += integrate.quad(integrand2, Tb_h2o, T.K)[0]
            return Entropy(JmolK=dSr)
