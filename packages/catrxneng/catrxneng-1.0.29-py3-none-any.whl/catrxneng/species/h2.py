from .species import Species
from ..quantities import *
from catrxneng import utils


class H2(Species):
    def __init__(self, T=None):
        self.mol_weight = 2
        self.Hf_298_gas = Energy(kJmol=0)
        self.S_298_gas = Entropy(JmolK=130.68)
        self.nist_thermo_params = [
            {
                "min_temp_K": 298,
                "max_temp_K": 1000,
                "phase": "gas",
                "A": 33.066178,
                "B": -11.363417,
                "C": 11.432816,
                "D": -2.772874,
                "E": -0.158558,
                "F": -9.980797,
                "G": 172.707974,
                "H": 0,
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
