import numpy as np

from ..kinetic_model import KineticModel
from catrxneng.utils import vant_hoff_eqn
from catrxneng.quantities import *


class Ghosh2022MTO(KineticModel):
    def __init__(self, limiting_reactant="ch3oh", T=None, kref=None, Ea=None):
        self.Tref = Temperature(C=320)
        self.components = [
            "ch3oh",
            "h2",
            "h2o",
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
        self.f8 = {
            "c2h4": 5e-2,
            "c3h6": 1.0,
            "c4h8": 2.6e-1,
        }
        self.f9 = {
            "c2h4": 5.5e-1,
            "c3h6": 1.0,
            "c4h8": 4.5e-1,
        }
        self.carbon_atoms = np.array([1, 0, 0, 2, 3, 4, 2, 3, 4, 6.5, 10.5, 0])
        self.kref = kref
        if self.kref is None: 
            self.kref = np.array([5.9e-1, 7e-2, 6e-1, 5.9e-2, 8e-2, 8.3e-1, 6e-2, 8.2e-1])
        self.Ea = Ea
        if self.Ea is None:
            self.Ea = np.array([70.0, 16.0, 17.0, 69.0, 109.0, 150.0, 170.0, 25.0])
        self.order = np.array([1, 2, 2, 2, 2, 1, 1, 2])
        self.comp_idx = {comp: i for i, comp in enumerate(self.components)}
        super().__init__(limiting_reactant, T)

    def compute_temp_dependent_constants(self):
        self.K_ch3oh = vant_hoff_eqn(1.3e1, Energy(kJmol=-2e-1), self.T, self.Tref).si
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
        p_c58 = p_array[self.comp_idx["c5-8"]]
        inhib = 1 + self.K_ch3oh * (p_ch3oh + p_h2o)

        n = 4
        r4 = self.k[4 - n] * p_ch3oh / inhib
        r5 = self.k[5 - n] * p_ch3oh * p_c2h4 / inhib
        r6 = self.k[5 - n] * p_ch3oh * p_c3h6 / inhib
        r7 = self.k[5 - n] * p_ch3oh * p_c4h8 / inhib
        r8_1 = self.k[8 - n] * p_c2h4 * p_h2 / inhib * self.f8["c2h4"]
        r8_2 = self.k[8 - n] * p_c3h6 * p_h2 / inhib * self.f8["c3h6"]
        r8_3 = self.k[8 - n] * p_c4h8 * p_h2 / inhib * self.f8["c4h8"]
        r9_1 = self.k[9 - n] * p_c2h4 / inhib * self.f9["c2h4"]
        r9_2 = self.k[9 - n] * p_c3h6 / inhib * self.f9["c3h6"]
        r9_3 = self.k[9 - n] * p_c4h8 / inhib * self.f9["c4h8"]
        r10_1 = self.k[10 - n] * p_c58 / inhib * self.f9["c2h4"]
        r10_2 = self.k[10 - n] * p_c58 / inhib * self.f9["c3h6"]
        r10_3 = self.k[10 - n] * p_c58 / inhib * self.f9["c4h8"]
        r11_1 = self.k[11 - n] * p_c2h4 * p_c58 / inhib * self.f9["c2h4"]
        r11_2 = self.k[11 - n] * p_c3h6 * p_c58 / inhib * self.f9["c3h6"]
        r11_3 = self.k[11 - n] * p_c4h8 * p_c58 / inhib * self.f9["c4h8"]

        return np.array(
            [
                -9 * r4 - 2 * r5 - 3 * r6 - 4 * r7,  # ch3oh
                -1 * r8_1 - r8_2 - r8_3,  # h2
                9 * r4 + 2 * r5 + 3 * r6 + 4 * r7,  # h2o
                r4 + r5 - r8_1 - r9_1 + r10_1 - r11_1,  # c2h4
                r4 + r6 - r8_2 - r9_2 + r10_2 - r11_2,  # c3h6
                r4 + r7 - r8_3 - r9_3 + r10_3 - r11_3,  # c4h8
                r8_1,  # c2h6
                r8_2,  # c3h8
                r8_3,  # c4h10
                0.307 * r9_1
                + 0.461 * r9_2
                + 0.615 * r9_3
                - 0.307 * r10_1
                - 0.461 * r10_2
                - 0.615 * r10_3
                - r11_1
                - r11_2
                - r11_3,  # c5-8
                0.809 * r11_1 + 0.904 * r11_2 + r11_3,  # c9+
                0.0,  # inert
            ]
        )
