from simple_graph import Graph


def dfs(graph: Graph, detect_back_edges=True):
    """Depth-first search implementation for Graph types"""
    # set colors to keep track of the exploration status
    color = {u: "white" for u in graph}
    # initialize the predecessor forest
    predecessor = {u: None for u in graph}
    # at the start no vertex was discovered
    discovery = {u: None for u in graph}
    # no vertices have been fully explored
    finalization = {u: None for u in graph}
    # initialize counter for node time stamping
    time = 0
    # keep track of back edges
    if detect_back_edges:
        back_edges = {}

    def dfs_visit(graph: Graph, u, time):
        time += 1
        discovery[u] = time
        color[u] = "gray"
        for v in graph.get_neighbors(u):
            if color[v] == "white":
                predecessor[v] = u
                dfs_visit(graph, v, time)
            if detect_back_edges and [v] == "gray":
                back_edges[u] = v
        color[u] = "black"
        time += 1
        finalization[u] = time

    # visit every unexplored vertex in the graph
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, time)
    #    print(f"back_edges = {back_edges}")

    if detect_back_edges:
        return predecessor, discovery, finalization, back_edges
    return predecessor, discovery, finalization
