from catrxneng import utils
from .species import Species
from ..quantities import *


class CO2(Species):
    CLASS = "carbon_oxide"
    C_ATOMS = 1
    O_ATOMS = 2
    MOL_WEIGHT = 44
    HF_298_GAS = Energy(kJmol=-393.51)
    S_298_GAS = Entropy(JmolK=213.79)
    NIST_THERMO_PARAMS = [
        {
            "min_temp_K": 298,
            "max_temp_K": 1200,
            "phase": "gas",
            "A": 24.99735,
            "B": 55.18696,
            "C": -33.69137,
            "D": 7.948387,
            "E": -0.136638,
            "F": -403.6075,
            "G": 228.2431,
            "H": -393.5224,
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
