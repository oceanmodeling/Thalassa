from __future__ import annotations

import logging

import holoviews as hv
import panel as pn
from holoviews import opts as hvopts

import thalassa.ui
from thalassa.utils import setup_logging

# configure logging
setup_logging()

# load bokeh
# hv.extension("bokeh")
# pn.extension(sizing_mode="fixed")

# pn.config.sizing_mode="fixed"
# pn.config.sizing_mode="stretch_width"
# pn.config.sizing_mode="scale_width"

# Set some defaults for the visualization of the graphs
# hvopts.defaults(
#     hvopts.Table(
#         height=300,
#     ),
#     hvopts.Curve(
#         responsive=False,
#         height=300,
#         show_title=True,
#         tools=["hover"],
#         active_tools=["pan", "wheel_zoom"],
#     ),
#     hvopts.Image(
#         height=500,
#         show_title=True,
#         tools=["hover"],
#         active_tools=["pan", "wheel_zoom"],
#     ),
# )


ui = thalassa.ui.ThalassaUI()

# https://panel.holoviz.org/reference/templates/Bootstrap.html
bootstrap = pn.template.ReactTemplate(
    # bootstrap = pn.template.BootstrapTemplate(
    # bootstrap = pn.template.FastListTemplate(
    # bootstrap = pn.template.MaterialTemplate(
    # site="example.com",
    title="Thalassa",
    # theme="dark",
    # logo="thalassa/static/logo.png",
    # favicon="thalassa/static/favicon.png",
    sidebar=[ui.sidebar],
    # sidebar_width=350,  # in pixels! must be an integer!
    # main_max_width="1350px", #  must be a string!
    main=[ui.main],
    # main_layout = "",
)

bootstrap.header_background="#2A6589"
bootstrap.sidebar.append(
    pn.Column(
        # pn.layout.VSpacer(height=100),
        pn.layout.VSpacer(),
        pn.pane.Markdown('''
        Powered by:
        <a href="https://github.com/ec-jrc/pyPoseidon/" style="color: #752A89" target="blank">pyPoseidon</a>
        <a href="https://github.com/ec-jrc/Thalassa/" style="color: #752A89" target="blank">Thalassa</a>
        <a href="http://ccrm.vims.edu/schismweb/" style="color: #752A89" target="blank">SCHISM</a>
        '''),
        # pn.layout.VSpacer(height=100),
    )
)

_ = bootstrap.servable()
