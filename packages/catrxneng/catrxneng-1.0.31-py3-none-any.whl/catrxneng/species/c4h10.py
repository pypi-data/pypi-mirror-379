from .species import Species
from ..quantities import *


class C4H10(Species):
    CLASS = "alkane"
    C_ATOMS = 4
    H_ATOMS = 10
    MOL_WEIGHT = 58.124

    def __init__(self, T=None):
        super().__init__(T)
