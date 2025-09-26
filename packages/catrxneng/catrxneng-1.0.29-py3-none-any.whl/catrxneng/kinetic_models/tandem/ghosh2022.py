import numpy as np

from ..kinetic_model import KineticModel
from ..co2_to_ch3oh import Ghosh2021
from ..mto import Ghosh2022MTO
from catrxneng.quantities import *


class Ghosh2022(KineticModel):
    def __init__(self, co2_mto_catalyst_ratio, limiting_reactant="co2", T=None):
        self.mass_frac_co2_to_meoh_catalyst = co2_mto_catalyst_ratio / (
            1 + co2_mto_catalyst_ratio
        )
        self.mass_frac_mto_catalyst = 1 - self.mass_frac_co2_to_meoh_catalyst
        self.km1 = Ghosh2021(T=T)
        self.km2 = Ghosh2022MTO(T=T)
        self.components = [
            "co2",
            "h2",
            "ch3oh",
            "h2o",
            "co",
            "ch4",
            "c2h4",
            "c3h6",
            "c4h8",
            "c2h6",
            "c3h8",
            "c4h10",
            "c5-8",
            "c9+",
            "inert",
        ]
        self.carbon_atoms = np.array([1, 0, 1, 0, 1, 1, 2, 3, 4, 2, 3, 4, 6.5, 10.5, 0])
        self.km1_map = [self.components.index(comp) for comp in self.km1.components]
        self.km2_map = [self.components.index(comp) for comp in self.km2.components]
        super().__init__(limiting_reactant, T)

    def set_temp(self, T):
        self.T = T
        self.km1.T = T
        self.km2.T = T

    def compute_temp_dependent_constants(self):
        self.km1.compute_temp_dependent_constants()
        self.km2.compute_temp_dependent_constants()

    def rate_equations(self, p_array):
        r1 = self.km1.rate_equations(p_array[self.km1_map])
        r1 = r1 * self.mass_frac_co2_to_meoh_catalyst
        r2 = self.km2.rate_equations(p_array[self.km2_map])
        r2 = r2 * self.mass_frac_mto_catalyst
        return np.array(
            [
                r1[0],  # co2
                r1[1] + r2[1],  # h2
                r1[2] + r2[0],  # ch3oh
                r1[3] + r2[2],  # h2o
                r1[4],  # co
                r1[5],  # ch4
                r2[3],  # c2h4
                r2[4],  # c3h6
                r2[5],  # c4h8
                r2[6],  # c2h6
                r2[7],  # c3h8
                r2[8],  # c4h10
                r2[9],  # c5-8
                r2[10],  # c9+
                0.0,  # inert
            ]
        )

    # def compute_selectivity(self, reactor):
    #     products = ("ch3oh", "co", "ch4", "G")
    #     sel = {}
    #     F_prod = reactor.F["co"] + reactor.
    #     sel["co"]
