from typing import List, Any

from aqt import mw

from .graphs import get_library


def make_graph_js(graphs: List[str], query: str = "") -> str:
    graph_string = ",\n".join(graphs)

    return f"""
anki.graphs(document.getElementById("graphsSection"), [
    {graph_string},
], {{
    search: `{query}`,
    days: 0,
}})
"""


class ProfileConfig:
    """Can be used for profile-specific settings"""

    def __init__(self, keyword: str, default: Any):
        self.keyword = keyword
        self.default = default

    @property
    def value(self) -> Any:
        return mw.pm.profile.get(self.keyword, self.default)

    @value.setter
    def value(self, new_value: Any):
        mw.pm.profile[self.keyword] = new_value

    def remove(self):
        try:
            del mw.pm.profile[self.keyword]
        except KeyError:
            # same behavior as Collection.remove_config
            pass


default_graphs = [
    ["CalendarGraph", True],
    ["FutureDue", True],
]


graphs_deckbrowser = ProfileConfig("statsPlusGraphsDeckbrowser", default_graphs)
graphs_overview = ProfileConfig("statsPlusGraphsOverview", default_graphs)


def get_active_graphs(graphs: List[str]) -> List[str]:
    active_graphs = [graph[0] for graph in graphs if graph[1]]
    qualified_graphs = [f"{get_library(graph)}.{graph}" for graph in active_graphs]

    return qualified_graphs


def get_active_deckbrowser_graphs() -> List[str]:
    return get_active_graphs(graphs_deckbrowser.value)


def get_active_overview_graphs() -> List[str]:
    return get_active_graphs(graphs_overview.value)
