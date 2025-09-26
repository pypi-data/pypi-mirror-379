from catrxneng import utils
from .species import Species
from ..quantities import *


class CO2(Species):
    def __init__(self, T=None):
        self.mol_weight = 44
        self.Hf_298_gas = Energy(kJmol=-393.51)
        self.S_298_gas = Entropy(JmolK=213.79)
        self.nist_thermo_params = [
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
    