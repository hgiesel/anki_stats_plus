from typing import List


def make_graph_js(graphs: List[str], query: str = "") -> str:
    qualified_graphs = [f"anki.{str(graph)}" for graph in graphs]
    graph_string = ",\n".join(qualified_graphs)

    return f"""
anki.graphs(document.getElementById("graphsSection"), [
    {graph_string},
], {{
    search: `{query}`,
    days: 0,
}})
"""
