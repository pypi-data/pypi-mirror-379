import numpy as np

from ..kinetic_model import KineticModel
from catrxneng.utils import vant_hoff_eqn
from catrxneng.reactions import RWGS, CO2ToCH3OH, Sabatier
from catrxneng.quantities import *


class Ghosh2021(KineticModel):
    def __init__(self, limiting_reactant="co2", site_model="single", T=None, kref=None, Ea=None):
        self.site_model = site_model
        self.Tref = Temperature(C=300)
        self.components = ["co2", "h2", "ch3oh", "h2o", "co", "ch4", "inert"]
        self.carbon_atoms = np.array([1, 0, 1, 0, 1, 1, 0])
        self.reactions = {
            "co2_to_meoh": CO2ToCH3OH(),
            "rwgs": RWGS(),
            "sabatier": Sabatier(),
        }
        self.kref = kref
        if self.kref is None:
            self.kref = np.array([6.9e-4, 1.8e-3, 1.1e-4])
        self.Ea = Ea
        if self.Ea is None:
            self.Ea = np.array([35.7, 54.5, 42.5])
        self.order = np.array([2.0, 1.5, 1.0])
        self.comp_idx = {comp: i for i, comp in enumerate(self.components)}
        self.rxn_idx = {rxn: i for i, rxn in enumerate(self.reactions)}
        super().__init__(limiting_reactant, T)
        self.stoich_coeff = np.array(
            [
                [-1, -3, 1, 1, 0, 0, 0],
                [-1, -1, 0, 1, 1, 0, 0],
                [-1, -4, 0, 2, 0, 1, 0],
            ]
        )

    def compute_temp_dependent_constants(self):
        self.K_h2 = vant_hoff_eqn(0.76, Energy(kJmol=-12.5), self.T, self.Tref).si
        self.K_co2 = vant_hoff_eqn(0.79, Energy(kJmol=-25.9), self.T, self.Tref).si
        self.K_co2_to_meoh = self.reactions["co2_to_meoh"].Keq(self.T)
        self.K_rwgs = self.reactions["rwgs"].Keq(self.T)
        self.K_sabatier = self.reactions["sabatier"].Keq(self.T)
        self.Keq = np.array([self.K_co2_to_meoh, self.K_rwgs, self.K_sabatier])
        self.k = np.array(
            [
                RateConstant(
                    molskgcatbar=kref, Ea=Energy(kJmol=Ea), Tref=self.Tref, order=order
                )(self.T).molhgcatbar
                for kref, Ea, order in zip(self.kref, self.Ea, self.order)
            ]
        )

    def rate_equations(self, p_array):
        p_co2 = p_array[0]  # co2
        p_h2 = p_array[1]  # h2
        p_ch3oh = p_array[2]  # ch3oh
        p_h2o = p_array[3]  # h2o
        p_co = p_array[4]  # co
        p_ch4 = p_array[5]  # ch4

        inhib = (1 + self.K_co2 * p_co2 + np.sqrt(self.K_h2 * p_h2)) ** 2

        fwd = p_co2 * p_h2**3
        rev = p_ch3oh * p_h2o / self.K_co2_to_meoh
        numerator = self.k[0] * (fwd - rev) / (p_h2**2)
        r1 = numerator / inhib

        fwd = p_co2 * p_h2
        rev = p_co * p_h2o / self.K_rwgs
        numerator = self.k[1] * (fwd - rev) / np.sqrt(p_h2)
        r2 = numerator / inhib

        numerator = p_ch4 * p_h2o**2
        denom = p_co2 * p_h2**4 * self.K_sabatier
        if denom == 0:
            r3 = 0
        else:
            frac = (1 - numerator / denom) / inhib
            r3 = self.k[2] * np.sqrt(p_co2 * p_h2) * frac

        return np.array(
            [
                -r1 - r2 - r3,  # co2
                -3 * r1 - r2 - 4 * r3,  # h2
                r1,  # ch3oh
                r1 + r2 + 2 * r3,  # h2o
                r2,  # co
                r3,  # ch4
                0.0,  # inert
            ]
        )
