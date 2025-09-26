from catrxneng import utils
from .species import Species
from ..quantities import *


class CH4(Species):
    CLASS = "alkane"
    C_ATOMS = 1
    H_ATOMS = 4
    MOL_WEIGHT = 16
    HF_298_GAS = Energy(kJmol=-74.6)
    S_298_GAS = Entropy(JmolK=186.3)
    NIST_THERMO_PARAMS = [
        {
            "min_temp_K": 298,
            "max_temp_K": 1300,
            "phase": "gas",
            "A": -0.703029,
            "B": 108.4773,
            "C": -42.52157,
            "D": 5.862788,
            "E": 0.678565,
            "F": -76.84376,
            "G": 158.7163,
            "H": -74.87310,
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
