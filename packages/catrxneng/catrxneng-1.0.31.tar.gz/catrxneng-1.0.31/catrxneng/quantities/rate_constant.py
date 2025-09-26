import numpy as np

from catrxneng import utils
from . import Quantity, Temperature


class RateConstant(Quantity):
    def __init__(self, Ea, order, Tref=None, **kwargs):
        self.Ea = Ea
        self.order = order
        self.Tref = Tref
        if self.Tref:
            self.T = self.Tref
        else:
            self.T = Temperature(K=298)
        super().__init__(**kwargs)
        if self.Tref:
            self.kref_si = self.si
        else:
            self.k0_si = self.si

    @property
    def molskgcatPa(self):
        return self.si

    @molskgcatPa.setter
    def molskgcatPa(self, value):
        self.si = utils.to_float(value)

    @property
    def molhgcatbar(self):
        return self.si * 3600 / 1000 * (100000**self.order)

    @molhgcatbar.setter
    def molhgcatbar(self, value):
        self.si = utils.to_float(value / 3600 * 1000 / (100000**self.order))

    @property
    def molmingcatbar(self):
        return self.si * 60 / 1000 * (100000**self.order)

    @molmingcatbar.setter
    def molmingcatbar(self, value):
        self.si = utils.to_float(value / 60 * 1000 / (100000**self.order))

    @property
    def molskgcatbar(self):
        return self.si * (100000**self.order)

    @molskgcatbar.setter
    def molskgcatbar(self, value):
        self.si = utils.to_float(value / (100000**self.order))

    @property
    def Lgcatmin(self):
        from . import R

        return self.molmingcatbar * (R.LbarKmol * self.T.K) ** self.order

    @Lgcatmin.setter
    def Lgcatmin(self, value):
        from . import R

        self.molmingcatbar = value / ((R.LbarKmol * self.T.K) ** self.order)

    # def get_Lgcatmin(self, T):
    #     return self.molmingcatbar * (R.LbarKmol * T.K) ** self.order

    # def set_Lgcatmin(self, value, T):
    #     self.molmingcatbar = value / ((R.LbarKmol * T.K) ** self.order)

    def __call__(self, T):
        from . import R

        self.T = T
        if self.Tref is not None:
            si = self.kref_si * np.exp(
                -self.Ea.si / R.si * (1 / T.si - 1 / self.Tref.si)
            )
        else:
            si = self.si * np.exp(-self.Ea.si / R.si / T.si)
        new_rate_constant = RateConstant(
            Ea=self.Ea, order=self.order, Tref=self.Tref, si=si
        )
        new_rate_constant.T = T
        return new_rate_constant

    # def set_temp(self, T):
    #     self.T = T
    #     return self
