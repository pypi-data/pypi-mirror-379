from .species import Species
from ..quantities import *

class Graphite(Species):
    CLASS = "solid_carbon"
    C_ATOMS = 1
    MOL_WEIGHT = 12
    S_298 = Entropy(JmolK=5.6)
    
    def __init__(self, T=None):
        super().__init__(T)
    
    def Cp(self, T):
        return HeatCapacity(JmolK=8.23)
