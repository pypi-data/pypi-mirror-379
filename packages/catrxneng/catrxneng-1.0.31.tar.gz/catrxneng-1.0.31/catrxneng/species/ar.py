from .species import Species
from ..quantities import *


class Ar(Species):
    CLASS = "noble_gas"
    AR_ATOMS = 1
    MOL_WEIGHT = 40
    MIN_TEMP = Temperature(K=500)
    MAX_TEMP = Temperature(K=2000)
    HF_298 = Energy(kJmol=0)
    THERMO_PARAMS = {
        "A": 19.50583,
        "B": 19.88705,
        "C": -8.598535,
        "D": 1.369784,
        "E": 0.527601,
        "F": -4.935202,
        "G": 212.3900,
        "H": 0.0,
    }

    def __init__(self, T=None):
        super().__init__(T)
