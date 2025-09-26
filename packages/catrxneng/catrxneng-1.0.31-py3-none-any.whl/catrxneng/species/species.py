from ..quantities import *


class Species:
    CLASS = "species"
    C_ATOMS = 0
    H_ATOMS = 0
    O_ATOMS = 0
    N_ATOMS = 0

    def __init__(self, T=None):
        self.T = T
        # self.update()

    def _get_thermo_params(self, T):
        for thermo_params in self.NIST_THERMO_PARAMS:
            if thermo_params["min_temp_K"] <= T.K <= thermo_params["max_temp_K"]:
                return thermo_params
            raise ValueError(
                f"Temperature outside range for {type(self).__name__} thermodynamic parameters."
            )
