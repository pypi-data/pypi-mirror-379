from .species import Species
from ..quantities import *


class C4H8(Species):
    CLASS = "alkene"
    C_ATOMS = 4
    H_ATOMS = 8
    MOL_WEIGHT = 56.108

    def __init__(self, T=None):
        super().__init__(T)
