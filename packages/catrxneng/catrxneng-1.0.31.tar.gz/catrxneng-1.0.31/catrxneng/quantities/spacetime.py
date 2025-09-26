from .quantity import Quantity
from ..species import GasMixture
from catrxneng.utils import *


class SpaceTime(Quantity):

    def __init__(self, gas_mixture: GasMixture = None, **kwargs):
        self.gas_mixture = gas_mixture
        super().__init__(**kwargs)

    @property
    def molskgcat(self):
        return self.si

    @molskgcat.setter
    def molskgcat(self, value):
        self.si = to_float(value)

    @property
    def molhgcat(self):
        return self.si / 3600 * 1000

    @molhgcat.setter
    def molhgcat(self, value):
        self.si = to_float(value) * 3600 / 1000

    @property
    def smLhgcat(self):
        return self.si / 3600 / 22.4

    @smLhgcat.setter
    def smLhgcat(self, value):
        self.si = to_float(value) * 3600 * 22.4

    @property
    def h(self):
        try:
            return self.si / 1000 * self.gas_mixture.avg_mol_weight * 3600
        except TypeError:
            raise AttributeError("Spacetime has no gas mixture assigned.")

    @h.setter
    def h(self, value):
        try:
            self.si = value * 1000 / self.gas_mixture.avg_mol_weight / 3600
        except TypeError:
            raise AttributeError("Spacetime has no gas mixture assigned.")
