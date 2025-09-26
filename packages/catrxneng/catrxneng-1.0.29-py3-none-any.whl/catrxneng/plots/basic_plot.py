import plotly.graph_objects as go, numpy as np
from catrxneng.utils import plot_info_box


class BasicPlot:

    def __init__(self, title=None):
        self.fig = go.Figure()
        self.title = title
        self.right_axis = False

    def add_trace(self, x, y, name=None, mode="lines", yaxis="y1", hover_label=None, line_dash=None):
        if isinstance(y, (float, int)):
            if x is not None:
                xmin = np.min(x)
                xmax = np.max(x)
            x = [xmin, xmax]
            y = [y, y]
        hovertemplate = None
        if hover_label:
            hovertemplate = "<b>%{text}</b><br>X: %{x}<br>Y: %{y}<extra></extra>"
        trace_kwargs = dict(
            x=x,
            y=y,
            mode=mode,
            yaxis=yaxis,
            name=name,
            text=hover_label,
            hovertemplate=hovertemplate,
        )
        if line_dash:
            trace_kwargs["line"] = dict(dash=line_dash)
        trace = go.Scatter(**trace_kwargs)
        self.fig.add_trace(trace)

    def add_vertical_line(self, x, line_dash="dash", line_color="black", line_width=2):
        """
        Adds a vertical dashed line at the specified x-value.

        Args:
            x_value (float): The x-coordinate where the vertical line will be added.
            line_dash (str): The dash style of the line (default is "dash").
            line_color (str): The color of the line (default is "black").
            line_width (int): The width of the line (default is 2).
        """
        self.fig.add_shape(
            type="line",
            x0=x,
            x1=x,
            y0=0,
            y1=1,
            xref="x",
            yref="paper",
            line=dict(
                dash=line_dash,
                color=line_color,
                width=line_width,
            ),
        )

    def render(
        self,
        xlabel,
        ylabel,
        xrange=None,
        yrange=None,
        ylabel2=None,
        yrange2=None,
        info_text=None,
    ):
        if xrange is None:
            xrange = [None, None]
        if yrange is None:
            yrange = [None, None]
        if yrange2 is None:
            yrange2 = [None, None]

        top = 50
        width = 700
        if info_text is None:
            bottom = 50
            height = 400
        else:
            bottom = 110
            height = None

        yaxis2 = None
        if ylabel2:
            yaxis2 = dict(
                title=f"<b>{ylabel2}</b>",
                range=yrange2,
                showline=True,
                linecolor="black",
                linewidth=2,
                mirror=True,
                nticks=9,
                overlaying="y",
                side="right",
            )
        self.fig.update_layout(
            title=dict(text=f"<b>{self.title}</b>", x=0.5),
            xaxis_title=f"<b>{xlabel}</b>",
            yaxis_title=f"<b>{ylabel}</b>",
            width=width,
            height=height,
            margin=dict(t=top, b=bottom),
            yaxis=dict(
                range=yrange,
                showline=True,
                linecolor="black",
                linewidth=2,
                mirror=True,
                nticks=9,
            ),
            yaxis2=yaxis2,
            xaxis=dict(
                range=xrange,
                showline=True,
                linecolor="black",
                linewidth=2,
                mirror=True,
            ),
            legend=dict(x=1.05, y=1, xanchor="left", yanchor="top"),
            annotations=plot_info_box(info_text),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        self.fig.show()
