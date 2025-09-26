from .species import Species
from ..quantities import *


class C2H4(Species):
    def __init__(self, T=None):
        self.mol_weight = 28
        self.c_atoms = 2
        self.h_atoms = 4
        self.Hf_298 = Energy(kJmol=52.4)
        self.nist_thermo_params = [{
            "min_temp_K": 298,
            "max_temp_K": 1200,
            "phase": "gas",
            "A": -6.387880,
            "B": 184.4019,
            "C": -112.9718,
            "D": 28.49593,
            "E": 0.315540,
            "F": 48.17332,
            "G": 163.1568,
            "H": 52.46694
        }]
        super().__init__(T)
