from typing import List, Tuple, Optional

from dataclasses import dataclass


@dataclass(frozen=True)
class Graph:
    """Class for keeping track of an item in inventory."""

    library: str
    name: str
    display_name: str


anki_graphs = [
    Graph("anki", "TodayStats", "Today Stats"),
    Graph("anki", "FutureDue", "Future Due Graph"),
    Graph("anki", "CalendarGraph", "Calendar Graph"),
    Graph("anki", "ReviewsGraph", "Reviews Graph"),
    Graph("anki", "CardCounts", "Card Counts"),
    Graph("anki", "IntervalsGraph", "Review Intervals"),
    Graph("anki", "EaseGraph", "Card Ease Graph"),
    Graph("anki", "HourGraph", "Hourly Breakdown"),
    Graph("anki", "ButtonsGraph", "Answer Buttons Graph"),
    Graph("anki", "AddedGraph", "Added Graph"),
]


addon_graphs = [
    # TO ADD-ON DEVELOPERS:
    # please insert extra graphs in here
]


def get_available_graphs() -> List[Graph]:
    return anki_graphs + addon_graphs


def get_graph(name: str) -> Optional[Graph]:
    available_graphs = get_available_graphs()
    filtered = filter(lambda graph: graph.name == name, available_graphs)

    try:
        graph = next(filtered)
    except:
        graph = None

    return graph


def get_graph_by_display_name(display_name: str) -> Optional[Graph]:
    available_graphs = get_available_graphs()
    filtered = filter(lambda graph: graph.display_name == display_name, available_graphs)

    try:
        graph = next(filtered)
    except:
        graph = None

    return graph


def get_library(name: str) -> Optional[str]:
    if graph := get_graph(name):
        return graph.library

    return None


def get_display_name(name: str) -> Optional[str]:
    if graph := get_graph(name):
        return graph.display_name

    return None


def get_name_from_display_name(display_name: str) -> Optional[str]:
    if graph := get_graph_by_display_name(display_name):
        return graph.name

    return None


def update_graphs(graphs: List[Tuple[str, bool]]) -> List[Tuple[str, bool]]:
    available_graphs = get_available_graphs()

    names = [graph[0] for graph in graphs]
    available_names = [graph.name for graph in available_graphs]

    names_available = [name in available_names for name in names]
    graphs_available = [
        graph for graph in graphs if names_available[graphs.index(graph)]
    ]

    names_additional = [name for name in available_names if name not in names]
    graphs_additional = [[name, False] for name in names_additional]

    return graphs_available + graphs_additional
