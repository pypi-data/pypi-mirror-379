import numpy as np

from ..kinetic_model import KineticModel
from catrxneng.quantities import *
from catrxneng.reactors import PFR


class Lee2019(KineticModel):
    def __init__(self, limiting_reactant="ch3oh", T=None, kref=None, Ea=None):
        self.Tref = Temperature(C=450)
        self.components = [
            "ch4",
            "c2h4",
            "c3h6",
            "c3h8",
            "c4h8",
            "c4",
            "c5+",
            "ch3oh",
            "h2o",
            "inert",
        ]
        self.comp_idx = {comp: i for i, comp in enumerate(self.components)}
        self.carbon_atoms = np.array([1, 2, 3, 3, 4, 4, 5, 1, 0, 0])
        self.kref = kref
        if self.kref is None:
            self.kref = np.array([0.16, 7.16, 7.35, 0.39, 2.26, 0.29, 0.9, 0.53, 0.36])
        self.Ea = Ea
        if self.Ea is None:
            self.Ea = np.array([71.7, 44.15, 14.02, 3.8, 6.24, 6.24, 10.0, 13.02, 4.04])
        self.K_h2o = 6.05
        super().__init__(limiting_reactant, T)

    def compute_temp_dependent_constants(self):
        self.k = np.array(
            [
                RateConstant(
                    Lgcatmin=kref, Ea=Energy(kJmol=Ea), Tref=self.Tref, order=1
                )(self.T).molhgcatbar
                for kref, Ea in zip(self.kref, self.Ea)
            ]
        )

    def rate_equations(self, p_array):
        p_meoh = p_array[self.comp_idx["ch3oh"]]
        p_h2o = p_array[self.comp_idx["h2o"]]
        p_c2h4 = p_array[self.comp_idx["c2h4"]]
        p_c3h6 = p_array[self.comp_idx["c3h6"]]
        P = np.sum(p_array)
        if P == 0:
            y_h2o = 0
        else:
            y_h2o = p_h2o / P
        theta_w = 1 / (1 + self.K_h2o * y_h2o)
        r = np.array(
            [
                self.k[0] * theta_w * p_meoh,
                self.k[1] * theta_w * p_meoh,
                self.k[2] * theta_w * p_meoh,
                self.k[3] * theta_w * p_meoh,
                self.k[4] * theta_w * p_meoh,
                self.k[5] * theta_w * p_meoh,
                self.k[6] * theta_w * p_meoh,
                self.k[7] * theta_w * p_c2h4,
                self.k[8] * theta_w * p_c3h6,
            ]
        )
        return np.array(
            [
                r[0],  # ch4
                (r[1] - r[7]) / 2,  # c2h4
                (r[2] + r[7] - r[8]) / 3,  # c3h6
                r[3] / 3,  # c3h8
                (r[4] + r[8]) / 4,  # c4h8
                r[5] / 4,  # c4
                r[6] / 5,  # c5+
                np.sum([-r[i] for i in range(7)]),  # meoh
                np.sum([r[i] for i in range(7)]),  # h2o
                0.0,  # inert
            ]
        )
