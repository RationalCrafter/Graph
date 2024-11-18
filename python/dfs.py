from simple_graph import Graph


def dfs(graph: Graph):
    """Depth-first search implementation for Graph types"""
    color = {u: "white" for u in graph}
    predecessor = {u: None for u in graph}
    discovery = {u: None for u in graph}
    finalization = {u: None for u in graph}
    time = 0

    def dfs_visit(graph: Graph, u, time):
        time += 1
        discovery[u] = time
        color[u] = "gray"
        for v in graph.get_neighbors(u):
            if color[v] == "white":
                predecessor[v] = u
                dfs_visit(graph, v, time)
        color[u] = "black"
        time += 1
        finalization[u] = time

    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, time)

    return predecessor, discovery, finalization
