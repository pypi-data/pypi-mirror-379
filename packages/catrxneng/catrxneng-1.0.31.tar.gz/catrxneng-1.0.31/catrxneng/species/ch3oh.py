from .species import Species
from ..quantities import Energy, Entropy, Temperature


class CH3OH(Species):
    CLASS = "alcohol"
    C_ATOMS = 1
    H_ATOMS = 4
    O_ATOMS = 1
    MOL_WEIGHT = 32
    HF_298_LIQ = Energy(kJmol=-238.4)
    S_298_LIQ = Entropy(JmolK=127.19)
    HF_298_GAS = Energy(kJmol=-205)
    DH_VAP = Energy(kJmol=35.21)
    DS_VAP = Entropy(JmolK=104.6)
    BOILING_TEMP = Temperature(C=64.7)

    def __init__(self, T=None):
        super().__init__(T)

    def Cp_liq(self, T=None):
        from ..quantities import HeatCapacity

        if not T:
            T = self.T
        cp = 0.1955 * T.K + 22.419
        return HeatCapacity(JmolK=cp)

    def Cp_gas(self, T=None):
        from ..quantities import HeatCapacity

        if not T:
            T = self.T
        cp = 0.0656 * T.K + 26.21
        return HeatCapacity(JmolK=cp)
