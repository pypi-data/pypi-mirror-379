from catrxneng import utils
from .species import Species
from ..quantities import *


class CO(Species):
    CLASS = "carbon_oxide"
    C_ATOMS = 1
    O_ATOMS = 1
    MOL_WEIGHT = 28
    HF_298_GAS = Energy(kJmol=-110.53)
    S_298_GAS = Entropy(JmolK=197.66)
    NIST_THERMO_PARAMS = [
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
    
    def __init__(self, T=None):
        super().__init__(T)

    def Hf_gas(self, T=None):
        if not T:
            T = self.T
        return utils.Hf_shomate(T, self.NIST_THERMO_PARAMS[0])

    def S_gas(self, T=None):
        if not T:
            T = self.T
        return utils.S_shomate(T, self.NIST_THERMO_PARAMS[0])

    def Cp_gas(self, T=None):
        if not T:
            T = self.T
        return utils.Cp_shomate(T, self.NIST_THERMO_PARAMS[0])