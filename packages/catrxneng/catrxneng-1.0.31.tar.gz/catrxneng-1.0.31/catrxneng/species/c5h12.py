from .species import Species
from ..quantities import *


class C5H12(Species):
    CLASS = "alkane"
    C_ATOMS = 5 
    H_ATOMS = 12
    MOL_WEIGHT = 72.151

    def __init__(self, T=None):
        super().__init__(T)
