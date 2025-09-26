from catrxneng import utils
from .species import Species
from ..quantities import *


class CO(Species):
    def __init__(self, T=None):
        self.mol_weight = 28
        self.Hf_298_gas = Energy(kJmol=-110.53)
        self.S_298_gas = Entropy(JmolK=197.66)
        self.nist_thermo_params = [
            {
                "min_temp_K": 298,
                "max_temp_K": 1300,
                "phase": "gas",
                "A": 25.56759,
                "B": 6.096130,
                "C": 4.054656,
                "D": -2.671301,
                "E": 0.131021,
                "F": -118.0089,
                "G": 227.3665,
                "H": -110.5271,
            }
        ]
        super().__init__(T)

    def Hf_gas(self, T=None):
        if not T:
            T = self.T
        return utils.Hf_shomate(T, self.nist_thermo_params[0])

    def S_gas(self, T=None):
        if not T:
            T = self.T
        return utils.S_shomate(T, self.nist_thermo_params[0])

    def Cp_gas(self, T=None):
        if not T:
            T = self.T
        return utils.Cp_shomate(T, self.nist_thermo_params[0])