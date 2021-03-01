from anki.hooks import wrap

from aqt.gui_hooks import overview_will_render_content
from aqt.overview import Overview

from .utils import make_graph_js, get_active_overview_graphs, add_browser_search_link


def add_graphs_to_overview(self, content):
    graph_js = make_graph_js(get_active_overview_graphs(), "deck:current")

    content.table += f"""
<div id="graphsSection"></div>
<script>
{graph_js}
</script>"
"""


def init_overview():
    overview_will_render_content.append(add_graphs_to_overview)
    Overview._linkHandler = wrap(Overview._linkHandler, add_browser_search_link, "before")
