from .species import Species
from ..quantities import *


class C3H6(Species):
    CLASS = "alkene"
    C_ATOMS = 3
    H_ATOMS = 6
    MOL_WEIGHT = 42.081

    def __init__(self, T=None):
        super().__init__(T)
