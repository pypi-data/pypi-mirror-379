from .species import Species
from ..quantities import *


class C2H4(Species):
    CLASS = "alkene"
    C_ATOMS = 2
    H_ATOMS = 4
    MOL_WEIGHT = 28
    HF_298 = Energy(kJmol=52.4)
    NIST_THERMO_PARAMS = [
        {
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
            "H": 52.46694,
        }
    ]

    def __init__(self, T=None):
        super().__init__(T)
