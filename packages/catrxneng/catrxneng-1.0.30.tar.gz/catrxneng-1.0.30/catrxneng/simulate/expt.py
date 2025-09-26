import os, requests, pandas as pd

from catrxneng import conf, utils
from catrxneng.utils import Influx, Time
from catrxneng.quantities import *


class Expt:

    @property
    def time_on_stream_hr(self):
        try:
            return (self.time_series_data["timestamp"] - self.t0) / 3600
        except AttributeError:
            raise AttributeError("Experiment has no t0 value assigned.")

    @property
    def steady_state_steps(self):
        return [step for step in self.steps if step.step_name == "steadyState"]

    def __init__(
        self,
        expt_type,
        reactor_class,
        kinetic_model,
        step_class,
        catalyst,
        mcat,
        unit,
        lab_notebook_id,
        T=None,
        p0=None,
        whsv=None,
    ):
        self.expt_type=expt_type
        self.reactor_class = reactor_class
        self.kinetic_model = kinetic_model
        self.step_class = step_class
        self.catalyst = catalyst
        self.mcat = mcat
        self.unit = unit
        self.lab_notebook_id = lab_notebook_id
        self.T = T
        self.p0 = p0
        self.whsv = whsv
        self.steps = []

    def add_step(self, step_name, start=None, end=None, T=None, p0=None, whsv=None):
        if start is None:
            start = self.steps[-1].end
        if end is None:
            end = start + TimeDelta(hr=1)
        if T is None:
            T = self.T
        if p0 is None:
            p0 = self.p0
        if whsv is None:
            whsv = self.whsv
        if T is None or p0 is None or whsv is None:
            raise ValueError("Step has a missing condition.")
        step = self.step_class(step_name, len(self.steps) + 1, start, end)
        step.attach_reactor(
            self.reactor_class, self.kinetic_model, T, p0, whsv, self.mcat
        )
        self.steps.append(step)

    def simulate(self, dt_sec, std_dev=None):
        for step in self.steps:
            step.simulate(dt_sec, std_dev)
        dataframes = [step.time_series_data for step in self.steps]
        self.time_series_data = pd.concat(dataframes, ignore_index=True)
        self._compute_tos()

    def upload_data(self, bucket, measurement):
        influx = Influx(
            url=os.getenv("INFLUXDB_URL"),
            org=os.getenv("INFLUXDB_ORG"),
            bucket=bucket,
            measurement=measurement,
        )
        # conf = utils.getconf(self.unit, "tags")
        # tags = [
        #     conf[data_id]
        #     for data_id in self.time_series_data.columns
        #     if data_id in conf
        # ]
        df = self.time_series_data.rename(columns=utils.getconf(self.unit, "tags"))
        influx.upload_dataframe(dataframe=df)

    def _compute_tos(self):
        for step in self.steps:
            if step.step_name == "steadyState":
                start = step.start.UET
                break
        self.tos = self.time_series_data["timestamp"] - start

    def upload_to_emp(self, host, dt_sec, notes=None):
        # url = "http://192.168.215.193:5001/10057/api"
        endpoint = "/api/create_simulated_expt/10057"
        url = host + endpoint
        params = {
            "expt_type": self.expt_type,
            "lab_notebook_id": self.lab_notebook_id,
            "unit": self.unit,
            "material__common_name": self.catalyst,
            "sample_mass": self.mcat.g,
            "start__ET_str": self.steps[0].start.ET_str,
            "end__ET_str": self.steps[-1].end.ET_str,
            "dt_sec": dt_sec,
            "notes": notes,
        }
        return requests.post(url, json=params, timeout=10).json()
