from .species import Species
from ..quantities import *


class C5H10(Species):
    CLASS = "alkene"
    C_ATOMS = 5
    H_ATOMS = 10
    MOL_WEIGHT = 70.135

    def __init__(self, T=None):
        super().__init__(T)
