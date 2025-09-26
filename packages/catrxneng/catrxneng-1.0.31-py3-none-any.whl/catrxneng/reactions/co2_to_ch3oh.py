import scipy.integrate as integrate

from .reaction import Reaction
from ..quantities import *
from ..species import *


class CO2ToCH3OH(Reaction):

    def __init__(self, T=None, limiting_reactant="co2"):
        self.components = {
            "co2": CO2(T=T),
            "h2": H2(T=T),
            "ch3oh": CH3OH(T=T),
            "h2o": H2O(T=T),
            "inert": Ar(T=T),
        }
        self.stoich_coeff = Unitless(
            si=[-1.0, -3.0, 1.0, 1.0, 0.0], keys=list(self.components.keys())
        )
        super().__init__(T=T, limiting_reactant=limiting_reactant)

    def dCp_1(self, T_K):
        T = Temperature(K=T_K)
        dCp = CH3OH().Cp_liq(T) + H2O().Cp_liq(T) - CO2().Cp_gas(T) - 3 * H2().Cp_gas(T)
        return dCp.JmolK

    def dCp_2(self, T_K):
        T = Temperature(K=T_K)
        dCp = CH3OH().Cp_gas(T) + H2O().Cp_liq(T) - CO2().Cp_gas(T) - 3 * H2().Cp_gas(T)
        return dCp.JmolK

    def dCp_3(self, T_K):
        T = Temperature(K=T_K)
        dCp = CH3OH().Cp_gas(T) + H2O().Cp_gas(T) - CO2().Cp_gas(T) - 3 * H2().Cp_gas(T)
        return dCp.JmolK

    @property
    def dH_rxn_298(self):
        return CH3OH().HF_298_LIQ + H2O().HF_298_LIQ - CO2().HF_298_GAS - 3 * H2().HF_298_GAS

    @property
    def dS_rxn_298(self):
        return CH3OH().S_298_LIQ + H2O().S_298_LIQ - CO2().S_298_GAS - 3 * H2().S_298_GAS

    def dH_rxn(self, T):
        Tb_ch3oh = CH3OH().BOILING_TEMP.K
        Tb_h2o = H2O().BOILING_TEMP.K
        if T.K < Tb_ch3oh:
            dHr = self.dH_rxn_298.Jmol
            dHr += integrate.quad(self.dCp_1, 298, T.K)[0]
            return Energy(Jmol=dHr)
        if Tb_ch3oh <= T.K < Tb_h2o :
            dHr = self.dH_rxn_298.Jmol
            dHr += integrate.quad(self.dCp_1, 298, Tb_ch3oh)[0]
            dHr += CH3OH().DH_VAP.Jmol
            dHr += integrate.quad(self.dCp_2, Tb_ch3oh, T.K)[0]
            return Energy(Jmol=dHr)
        if T.K >= Tb_h2o:
            dHr = self.dH_rxn_298.Jmol
            dHr += integrate.quad(self.dCp_1, 298, Tb_ch3oh)[0]
            dHr += CH3OH().DH_VAP.Jmol
            dHr += integrate.quad(self.dCp_2, Tb_ch3oh, Tb_h2o)[0]
            dHr += H2O().DH_VAP.Jmol
            dHr += integrate.quad(self.dCp_3, Tb_h2o, T.K)[0]
            return Energy(Jmol=dHr)

    def dS_rxn(self, T):
        Tb_ch3oh = CH3OH().BOILING_TEMP.K
        Tb_h2o = H2O().BOILING_TEMP.K
        integrand1 = lambda T_K: self.dCp_1(T_K) / T_K
        integrand2 = lambda T_K: self.dCp_2(T_K) / T_K
        integrand3 = lambda T_K: self.dCp_3(T_K) / T_K
        if T.K < Tb_ch3oh:
            dSr = self.dS_rxn_298.JmolK
            dSr += integrate.quad(integrand1, 298, T.K)[0]
            return Entropy(JmolK=dSr)
        if Tb_ch3oh <= T.K < Tb_h2o :
            dSr = self.dS_rxn_298.JmolK
            dSr += integrate.quad(integrand1, 298, Tb_ch3oh)[0]
            dSr += CH3OH().DS_VAP.JmolK
            dSr += integrate.quad(integrand2, Tb_ch3oh, T.K)[0]
            return Entropy(JmolK=dSr)
        if T.K >= Tb_h2o:
            dSr = self.dS_rxn_298.JmolK
            dSr += integrate.quad(integrand1, 298, Tb_ch3oh)[0]
            dSr += CH3OH().DS_VAP.JmolK
            dSr += integrate.quad(integrand2, Tb_ch3oh, Tb_h2o)[0]
            dSr += H2O().DS_VAP.JmolK
            dSr += integrate.quad(integrand3, Tb_h2o, T.K)[0]
            return Entropy(JmolK=dSr)
