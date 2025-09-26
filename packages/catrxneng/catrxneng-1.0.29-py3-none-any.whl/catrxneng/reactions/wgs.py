from .reaction import Reaction
from .. import species
from ..quantities import *
from .rwgs import RWGS


class WGS(Reaction):
    def __init__(self, T=None, limiting_reactant="co"):
        self.components = {
            "co": species.CO(T=T),
            "h2o": species.H2O(T=T),
            "co2": species.CO2(T=T),
            "h2": species.H2(T=T),
            "inert": species.Ar(T=T),
        }
        self.stoich_coeff = Unitless(
            si=[-1.0, -1.0, 1.0, 1.0, 0.0], keys=list(self.components.keys())
        )
        super().__init__(T=Tk, limiting_reactant=limiting_reactant)

    def Keq(self, T=None):
        if not T:
            T = self.T
        return 1 / RWGS().Keq(T)
