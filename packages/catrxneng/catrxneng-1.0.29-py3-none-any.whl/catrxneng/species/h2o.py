from .species import Species

from catrxneng import utils


class H2O(Species):
    def __init__(self, T=None):
        from ..quantities import Energy, Entropy, Temperature

        self.mol_weight = 18
        self.Hf_298_liq = Energy(kJmol=-285.83)
        self.S_298_liq = Entropy(JmolK=69.95)
        self.Hf_298_gas = Energy(kJmol=-241.83)
        self.S_298_gas = Entropy(JmolK=188.84)
        self.boiling_temp = Temperature(C=100)
        self.dH_vap = Energy(kJmol=40.657)
        self.dS_vap = Entropy(JmolK=109)
        # self.Cp_liq = HeatCapacity(JmolK=75.3)
        self.nist_thermo_params = [
            {
                "min_temp_K": 298,
                "max_temp_K": 500,
                "phase": "liq",
                "A": -203.606,
                "B": 1523.29,
                "C": -3196.413,
                "D": 2474.455,
                "E": 3.855326,
                "F": -256.5487,
                "G": -488.7163,
                "H": -285.8304,
            },
            {
                "min_temp_K": 500,
                "max_temp_K": 1700,
                "phase": "gas",
                "A": 30.09200,
                "B": 6.832514,
                "C": 6.793435,
                "D": -2.534480,
                "E": 0.082139,
                "F": -250.8810,
                "G": 223.3967,
                "H": -241.8264,
            },
        ]
        super().__init__(T)

    def Cp_gas(self, T=None):
        from ..quantities import HeatCapacity

        if not T:
            T = self.T
        params = self.nist_thermo_params[1]
        if params["min_temp_K"] <= T.K <= params["max_temp_K"]:
            return utils.Cp_shomate(T, params)
        elif 298 <= T.K <= 500:
            return HeatCapacity(JmolK=34.52)
        else:
            raise ValueError("Invalid temperature for H2O Cp_gas.")

    def Cp_liq(self, T=None):
        if not T:
            T = self.T
        params = self.nist_thermo_params[0]
        if params["min_temp_K"] <= T.K <= params["max_temp_K"]:
            return utils.Cp_shomate(T, params)
        else:
            raise ValueError("Invalid temperature for H2O Cp_liq.")
