import numpy as np
from scipy.integrate import solve_ivp

from .. import utils
from ..quantities import *
from .reactor import Reactor
from catrxneng.species.gas_mixture import GasMixture


class PFR(Reactor):
    def __init__(
        self,
        kinetic_model,
        p0,
        whsv=None,
        T=None,
        limiting_reactant=None,
        mcat=None,
        F0=None,
    ):
        self.kinetic_model = kinetic_model
        self.p0 = p0
        self.P = np.sum(p0)
        self.P_bar = self.P.bar
        self.y0 = utils.divide(p0, self.P)
        self.whsv = whsv
        self.T = T
        if self.T is None:
            self.T = kinetic_model.T
        self.limiting_reactant = limiting_reactant
        if not self.limiting_reactant:
            self.limiting_reactant = self.kinetic_model.limiting_reactant
        self.mcat = mcat
        if not mcat:
            self.mcat = Mass(g=1)
        if self.whsv:
            if self.whsv.gas_mixture is None:
                self.whsv.gas_mixture = GasMixture(p=p0)
            self.Ft0_active = self.whsv * self.mcat
            self.Ft0 = self.Ft0_active / (1 - self.y0["inert"])
            self.F0 = self.y0 * self.Ft0
        else:
            self.F0 = F0
            self.Ft0 = MolarFlowRate(molh=np.sum(self.F0.molh))
            self.Ft0_active = self.Ft0 - self.F0["inert"]
            # self.Ft0_active = MolarFlowRate(
            #     molh=np.sum(
            #         [self.F0[comp].molh for comp in self.p0.keys if comp != "inert"]
            #     )
            # )
            gas_mixture = GasMixture(p=self.p0)
            self.whsv = WHSV(
                molhgcat=self.Ft0_active.molh / self.mcat.g, gas_mixture=gas_mixture
            )

        self.check_components()

    def dFdw(self, w, F):
        p_array = F / np.sum(F) * self.P_bar
        return self.kinetic_model.rate_equations(p_array)

    def dfdx(self, x, f):
        # Ft = np.sum(self.F0[self.limiting_reactant].si * f)
        Ft = np.sum(self.Ft0_active.si * f)
        p = self.P.si * self.Ft0_active.si * f / Ft
        p = Pressure(si=p, keys=self.p0.keys.copy())
        return (
            self.mcat.si
            / self.Ft0_active.si
            * np.array(
                [
                    rate(p, self.T).si
                    for rate in self.kinetic_model.rate_equations.values()
                ]
            )
        )

    def solve_dimensional(self, points, method):
        w_span = (0, self.mcat.g)
        w_eval = np.linspace(0, self.mcat.g, points)
        # F0 = getattr(self.F0, self.units["molar_flow_rate"])
        F0 = self.F0.molh
        solution = solve_ivp(self.dFdw, w_span, F0, t_eval=w_eval, method=method)
        self.w = Mass(g=solution.t)
        # kwargs = {self.units["molar_flow_rate"]: solution.y}
        # kwargs["keys"] = self.kinetic_model.components
        self.F = MolarFlowRate(molh=solution.y, keys=self.F0.keys)

    def solve_dimensionless(self, points=1000, method="RK45", rtol=1e-3, atol=1e-6):
        x_span = (0, 1)
        x_eval = np.linspace(x_span[0], x_span[1], points)
        f0 = self.F0.si / self.Ft0_active.si
        solution = solve_ivp(
            self.dfdx, x_span, f0, t_eval=x_eval, method=method, rtol=rtol, atol=atol
        )
        self.x = solution.t
        self.f = solution.y
        self.w = Mass(si=(self.x * self.mcat.si))
        F = self.Ft0_active.si * self.f
        self.F = MolarFlowRate(si=F, keys=self.F0.keys)

    def solve(self, points=100, nondimensionalize=False, method="LSODA"):
        if nondimensionalize:
            self.solve_dimensionless(points=points, method=method)
        else:
            self.solve_dimensional(points=points, method=method)
        self.y = utils.divide(self.F, np.sum(self.F, axis=0))
        self.conversion = utils.divide(
            self.F0[self.limiting_reactant] - self.F[self.limiting_reactant],
            self.F0[self.limiting_reactant],
        )
        # self.yield_ = self.F / self.F0[self.limiting_reactant]
        spacetime = utils.divide(self.w.g, self.Ft0.smLh)
        self.spacetime = SpaceTime(smLhgcat=spacetime)
        self.whsv_array = WHSV(smLhgcat=utils.divide(1, spacetime))
        vol_flow_rate = self.Ft0.si * R.si * self.T.si / self.P.si
        self.vol_flow_rate = VolumetricFlowRate(si=vol_flow_rate)
