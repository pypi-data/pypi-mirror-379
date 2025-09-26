from ..quantities import *


class Species:

    def __init__(self, T=None):
        self.T = T
        # self.update()

    def _get_thermo_params(self, T):
        for thermo_params in self.nist_thermo_params:
            if thermo_params["min_temp_K"] <= T.K <= thermo_params["max_temp_K"]:
                return thermo_params
            raise ValueError(
                f"Temperature outside range for {type(self).__name__} thermodynamic parameters."
            )
