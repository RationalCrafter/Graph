from adj_list_graph import AdjacencyListGraph
from adj_matrix_graph import AdjacencyMatrixGraph
from bfs import bfs


def main():
    print("AdjacencyListGraph example :")
    g = AdjacencyListGraph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_edge("a", "b")
    g.add_edge("a", "c")
    g.add_edge("b", "d")
    g.add_edge("c", "d")
    g.add_edge("d", "e")
    d, p = bfs(g, "a")
    print(f"distance={d}")
    print(f"predecessor={p}")
    print("AdjacencyMatrixGraph example :")
    g = AdjacencyMatrixGraph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_edge("a", "b")
    g.add_edge("a", "c")
    g.add_edge("b", "d")
    g.add_edge("c", "d")
    g.add_edge("d", "e")
    d, p = bfs(g, "a")

    print(f"distance={d}")
    print(f"predecessor={p}")


if __name__ == "__main__":
    main()
