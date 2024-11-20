from simple_graph import Graph
from dfs import dfs


def topological_sort(g: Graph):
    """Returns a topological sort of g, if one is possible.
    If the graph contains cycles, return None."""
    # the simplest solution is to simply call dfs and reverse the finalization times
    _, _, finalization, back_edges = dfs(g, detect_back_edges=True)
    if back_edges != {}:
        return None
    return [
        x[0]
        for x in sorted(
            [(n, finalization[n]) for n in finalization],
            key=lambda x: x[1],
            reverse=True,
        )
    ]
