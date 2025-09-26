import os, numpy as np, pandas as pd
from importlib import import_module

from .influx import Influx
from .time import Time


def get_keys(obj1, obj2):
    if getattr(obj1, "keys", None) == getattr(obj2, "keys", None):
        keys = getattr(obj1, "keys", None)
    if getattr(obj1, "keys", None) is not None:
        keys = obj1.keys
    if getattr(obj2, "keys", None) is not None:
        keys = obj2.keys
    try:
        if keys is None:
            return None
        else:
            return keys.copy()
    except NameError:
        raise ValueError("Quantities have mismatching keys.")


def rate_const(T, Ea, k0=None, kref=None, Tref=None):
    from ..quantities import R, RateConstant

    if kref and Tref:
        k0 = kref.si / (np.exp(-Ea / (R * Tref))).si
        k0 = RateConstant(si=k0, order=kref.order)

    k = k0.si * np.exp(-Ea / (R * T)).si
    return RateConstant(si=k, order=k0.order)


# def vant_hoff_eq_const(T, dH, Kref, Tref):
#     from ..quantities import R, EquilibriumConstant

#     Keq = Kref.si * np.exp(dH / R * (1 / Tref - 1 / T)).si
#     return EquilibriumConstant(si=Keq, order=Kref.order)


def to_float(value):
    if isinstance(value, (np.ndarray, pd.Series)):
        return value.astype(float)
    if isinstance(value, int):
        return float(value)
    return value


def plot_info_box(text):
    if text is None:
        return None
    text = text.replace("\\n", "\n")
    text = text.strip("\n")
    text = text.replace("\n", "<br>")
    annotations = [
        dict(
            x=0.5,
            y=-0.35,
            xref="paper",
            yref="paper",
            text=text,
            showarrow=False,
            font=dict(size=12, style="italic", weight="bold"),
        )
    ]
    return annotations


def divide(x, y):
    if isinstance(y, (np.ndarray, pd.Series)):
        y_safe = y.copy()
        y_safe[y_safe == 0] = np.nan
    else:
        y_safe = np.nan if y == 0 else y

    return x / y_safe


def getconf(conf_name, variable):
    conf_module_path = os.getenv("CONF_MODULE_PATH")
    # module_path = f"catrxneng.conf.{conf_name}"
    module_path = f"{conf_module_path}.{conf_name}"
    # try:
    conf_module = import_module(module_path)
    # except ModuleNotFoundError as e:
    #     raise ImportError(f"Configuration module '{module_path}' not found.") from e
    # try:
    return getattr(conf_module, variable)
    # except AttributeError as e:
    #     raise AttributeError(
    #         f"Variable '{variable}' not found in '{module_path}'."
    #     ) from e


def Hf_shomate(T, params):
    from catrxneng.quantities import Energy

    t = T.K / 1000
    dHf = (
        params["A"] * t
        + params["B"] * t**2 / 2
        + params["C"] * t**3 / 3
        + params["D"] * t**4 / 4
        - params["E"] / t
        + params["F"]
        - params["H"]
    )  # kJ/mol
    return Energy(kJmol=dHf)


def S_shomate(T, params):
    from catrxneng.quantities import Entropy

    t = T.K / 1000
    S = (
        params["A"] * np.log(t)
        + params["B"] * t
        + params["C"] * t**2 / 2
        + params["D"] * t**3 / 3
        - params["E"] / (2 * t**2)
        + params["G"]
    )  # J/mol/K
    return Entropy(JmolK=S)


def Cp_shomate(T, params):
    from catrxneng.quantities import HeatCapacity

    t = T.K / 1000
    Cp = (
        params["A"]
        + params["B"] * t
        + params["C"] * t**2
        + params["D"] * t**3
        + params["E"] / (t**2)
    )
    return HeatCapacity(JmolK=Cp)


def vant_hoff_eqn(x_ref, dH, T, Tref):
    from catrxneng.quantities import R

    return x_ref * np.exp(dH / R * (1 / Tref - 1 / T))
