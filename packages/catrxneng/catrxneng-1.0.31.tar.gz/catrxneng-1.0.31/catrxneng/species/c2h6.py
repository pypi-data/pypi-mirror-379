from .species import Species
from ..quantities import *


class C2H6(Species):
    CLASS = "alkane"
    C_ATOMS = 2
    H_ATOMS = 6
    MOL_WEIGHT = 30.07

    def __init__(self, T=None):
        super().__init__(T)
