from simple_graph import Graph


def dfs(graph: Graph, detect_back_edges=False):
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
    time = [0]  # Use a list to maintain state across recursive calls
    # keep track of back edges
    if detect_back_edges:
        back_edges = {}

    def dfs_visit(graph: Graph, u):
        color[u] = "gray"
        time[0] += 1  # Increment the time and update discovery time
        discovery[u] = time[0]

        for v in graph.get_neighbors(u):
            if color[v] == "white":
                predecessor[v] = u
                dfs_visit(graph, v)
            if detect_back_edges and color[v] == "gray":
                back_edges[u] = v

        color[u] = "black"
        time[0] += 1  # Increment time again for finalization
        finalization[u] = time[0]

    # Visit every unexplored vertex in the graph
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u)

    if detect_back_edges:
        return predecessor, discovery, finalization, back_edges
    return predecessor, discovery, finalization
