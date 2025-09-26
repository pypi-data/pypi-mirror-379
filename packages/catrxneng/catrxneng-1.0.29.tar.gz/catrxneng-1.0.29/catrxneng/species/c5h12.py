from .species import Species
from ..quantities import *


class C5H12(Species):
    def __init__(self, T=None):
        self.mol_weight = 72.151
        self.c_atoms = 5
        self.h_atoms = 12
        super().__init__(T)
