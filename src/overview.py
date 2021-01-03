from aqt.gui_hooks import overview_will_render_content

from .utils import make_graph_js


def add_graphs_to_overview(self, content):
    graph_js = make_graph_js(["CalendarGraph", "CardCounts"], "deck:current")

    content.table += '<div id="graphsSection"></div>' f"<script>{graph_js}</script>"


def init_overview():
    overview_will_render_content.append(add_graphs_to_overview)
