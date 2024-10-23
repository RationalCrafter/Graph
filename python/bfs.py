from collections import deque
from simple_graph import Graph


def bfs(graph: Graph, s):
    """Breadth first search implementation for graph types."""
    # set properties for graph nodes
    # color encodes the exploration status:
    # white = unexplored, gray = discovered, black = fully explored
    color = {u: "white" for u in graph}
    # distance keeps track of the number of edges from the starting node s
    distance = {u: float("inf") for u in graph}
    # predecessor keeps track of the previous node in the bfs tree
    predecessor = {u: None for u in graph}
    # set properties for the source node
    color[s] = "gray"  # discovered by default at initialization
    distance[s] = 0  # distance to itself must be 0
    queue = deque()
    queue.append(s)
    while queue:
        u = queue.pop()
        #        print(u)
        for v in graph.get_neighbors(u):
            #            print(v)
            v = v[0]
            if color[v] == "white":
                color[v] = "gray"
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)
        color[u] = "black"
    return distance, predecessor
