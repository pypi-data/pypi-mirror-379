from .species import Species


class DME(Species):
    CLASS = "ether"
    C_ATOMS = 2
    H_ATOMS = 6
    O_ATOMS = 1
    MOL_WEIGHT = 46.069

    def __init__(self, T=None):
        from ..quantities import Energy, Entropy, Temperature

        # self.Hf_298_liq = Energy(kJmol=-238.4)
        # self.S_298_liq = Entropy(JmolK=127.19)
        # self.Hf_298_gas = Energy(kJmol=-205)
        # self.dH_vap = Energy(kJmol=35.21)
        # self.dS_vap = Entropy(JmolK=104.6)
        # self.boiling_temp = Temperature(C=64.7)
        super().__init__(T)

    # def Cp_liq(self, T=None):
    #     from ..quantities import HeatCapacity

    #     if not T:
    #         T = self.T
    #     cp = 0.1955 * T.K + 22.419
    #     return HeatCapacity(JmolK=cp)

    # def Cp_gas(self, T=None):
    #     from ..quantities import HeatCapacity

    #     if not T:
    #         T = self.T
    #     cp = 0.0656 * T.K + 26.21
    #     return HeatCapacity(JmolK=cp)
