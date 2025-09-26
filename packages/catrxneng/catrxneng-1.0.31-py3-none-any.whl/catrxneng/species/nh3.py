from .species import Species
from ..quantities import *


class NH3(Species):
    CLASS = "inorganic_hydride"
    H_ATOMS = 3
    N_ATOMS = 1
    MOL_WEIGHT = 17
    MIN_TEMP = Temperature(K=298)
    MAX_TEMP = Temperature(K=1400)
    HF_298 = Energy(kJmol=-45.9)
    THERMO_PARAMS = {
        "A": 19.99563,
        "B": 49.77119,
        "C": -15.37599,
        "D": 1.921168,
        "E": 0.189174,
        "F": -53.30667,
        "G": 203.8591,
        "H": -45.89806,
    }

    def __init__(self, T=None):
        super().__init__(T)
