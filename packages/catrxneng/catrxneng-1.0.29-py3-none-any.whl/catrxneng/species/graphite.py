from .species import Species
from ..quantities import *

class Graphite(Species):
    def __init__(self, T=None):
        self.mol_weight = 12
        self.S_298 = Entropy(JmolK=5.6)
        super().__init__(T)
    
    def Cp(self, T):
        return HeatCapacity(JmolK=8.23)
