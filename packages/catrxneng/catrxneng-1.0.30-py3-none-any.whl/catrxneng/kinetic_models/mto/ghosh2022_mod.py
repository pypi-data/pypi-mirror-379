import numpy as np

from ..kinetic_model import KineticModel
from catrxneng.utils import vant_hoff_eqn
from catrxneng.quantities import *


class Ghosh2022Mod(KineticModel):
    def __init__(self, limiting_reactant="ch3oh", T=None, kref=None, Ea=None):
        self.Tref = Temperature(C=320)
        self.components = [
            "ch3oh",
            "h2",
            "h2o",
            "c2h4",
            "c3h6",
            "c4h8",
            "c5h10",
            "c2h6",
            "c3h8",
            "c4h10",
            "c5h12",
            "inert",
        ]
        self.carbon_atoms = np.array([1, 0, 0, 2, 3, 4, 5, 2, 3, 4, 5, 0])
        self.kref = kref
        if self.kref is None:
            k2 = 0.001
            self.kref = np.array([1000, 800, 600, 400, k2, k2, k2, k2])
        self.Ea = Ea
        if self.Ea is None:
            Ea1 = 70.0
            Ea2 = 110.0
            self.Ea = np.array([Ea1, Ea1, Ea1, Ea1, Ea2, Ea2, Ea2, Ea2])
        self.order = np.array([1, 1, 1, 1, 2, 2, 2, 2])
        self.comp_idx = {comp: i for i, comp in enumerate(self.components)}
        super().__init__(limiting_reactant, T)

    def compute_temp_dependent_constants(self):
        self.K_ch3oh = vant_hoff_eqn(1.3e1, Energy(kJmol=-2e-1), self.T, self.Tref).si
        self.K_h2o = vant_hoff_eqn(1e1, Energy(kJmol=-2e-1), self.T, self.Tref).si
        self.k = np.array(
            [
                RateConstant(
                    molskgcatbar=kref, Ea=Energy(kJmol=Ea), Tref=self.Tref, order=order
                )(self.T).molhgcatbar
                for kref, Ea, order in zip(self.kref, self.Ea, self.order)
            ]
        )

    def rate_equations(self, p_array):
        p_ch3oh = p_array[self.comp_idx["ch3oh"]]
        p_h2 = p_array[self.comp_idx["h2"]]
        p_h2o = p_array[self.comp_idx["h2o"]]
        p_c2h4 = p_array[self.comp_idx["c2h4"]]
        p_c3h6 = p_array[self.comp_idx["c3h6"]]
        p_c4h8 = p_array[self.comp_idx["c4h8"]]
        p_c5h10 = p_array[self.comp_idx["c5h10"]]
        inhib = 1 + self.K_ch3oh * p_ch3oh + self.K_h2o * p_h2o

        r_c2h4 = self.k[0] * p_ch3oh / inhib
        r_c3h6 = self.k[1] * p_ch3oh / inhib
        r_c4h8 = self.k[2] * p_ch3oh / inhib
        r_c5h10 = self.k[3] * p_ch3oh / inhib
        r_c2h6 = self.k[4] * p_c2h4 * p_h2 / inhib
        r_c3h8 = self.k[5] * p_c3h6 * p_h2 / inhib
        r_c4h10 = self.k[6] * p_c4h8 * p_h2 / inhib
        r_c5h12 = self.k[7] * p_c5h10 * p_h2 / inhib

        return np.array(
            [
                -2 * r_c2h4 - 3 * r_c3h6 - 4 * r_c4h8 - 5 * r_c5h10,  # meoh
                -r_c2h4 - r_c3h6 - r_c4h8 - r_c5h10,  # h2
                2 * r_c2h4 + 3 * r_c3h6 + 4 * r_c4h8 + 5 * r_c5h10,  # h2o 
                r_c2h4 - r_c2h6, # c2h4
                r_c3h6 - r_c3h8, # c3h6
                r_c4h8 - r_c4h10, # c4h8
                r_c5h10 - r_c5h12, # c5h10
                r_c2h6, # c2h6
                r_c3h8, # c3h8
                r_c4h10, # c4h10
                r_c5h12, # c5h12
                0.0,  # inert
            ]
        )
