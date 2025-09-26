from .species import Species
from ..quantities import *


class C3H8(Species):
    CLASS = "alkane"
    C_ATOMS = 3
    H_ATOMS = 8
    MOL_WEIGHT = 44.097

    def __init__(self, T=None):
        super().__init__(T)
