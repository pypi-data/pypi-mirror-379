from catrxneng import utils
from .species import Species
from ..quantities import *


class CH4(Species):
    def __init__(self, T=None):
        self.mol_weight = 16
        self.Hf_298_gas = Energy(kJmol=-74.6)
        self.S_298_gas = Entropy(JmolK=186.3)
        self.nist_thermo_params = [
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