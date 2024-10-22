import cProfile
import timeit
import time
from memory_profiler import profile
import adj_list_graph
import adj_matrix_graph

timing_header = ["add_vertex", "add_edge", "has_vertex", "add_edge"]


def bench5v5e_adj_list(num_rep=1):
    for _ in range(num_rep):
        g = adj_list_graph.AdjacencyListGraph()
        # add vertices
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_vertex("D")
        g.add_vertex("E")
        # add edges
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        g.add_edge("C", "E")
        g.add_edge("D", "E")
        # has_vertex
        g.has_vertex("A")
        g.has_vertex("B")
        g.has_vertex("C")
        g.has_vertex("D")
        g.has_vertex("E")
        g.has_vertex("F")  # non existent
        g.has_vertex("G")  # non existent
        g.has_vertex("H")  # non existent
        # has_edge
        g.has_edge("A", "B")
        g.has_edge("A", "C")
        g.has_edge("B", "D")
        g.has_edge("C", "E")
        g.has_edge("D", "E")
        g.has_edge("A", "E")
        g.has_edge("B", "A")


def bench5v5e_adj_matrix(num_rep=1):
    for _ in range(num_rep):
        g = adj_matrix_graph.AdjacencyMatrixGraph()
        # add vertices
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_vertex("D")
        g.add_vertex("E")
        # add edges
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        g.add_edge("C", "E")
        g.add_edge("D", "E")
        # has_vertex
        g.has_vertex("A")
        g.has_vertex("B")
        g.has_vertex("C")
        g.has_vertex("D")
        g.has_vertex("E")
        g.has_vertex("F")  # non existent
        g.has_vertex("G")  # non existent
        g.has_vertex("H")  # non existent
        # has_edge
        g.has_edge("A", "B")
        g.has_edge("A", "C")
        g.has_edge("B", "D")
        g.has_edge("C", "E")
        g.has_edge("D", "E")
        g.has_edge("A", "E")
        g.has_edge("B", "A")


def bench10v_fully_connected(graph_class):
    g = graph_class()
    # add vertices
    for i in range(10):
        g.add_vertex(i)
    # add edges between every pair of vertices
    for i in range(10):
        for j in range(10):
            g.add_edge(i, j)
    # check every single vertex and a few that don't exist
    for i in range(20):
        g.has_vertex(i)
    # check every existing edge and a few that don't exist
    for i in range(20):
        for j in range(20):
            g.has_edge(i, j)


@profile
def benchmark_mgraph():
    start_time = time.time()

    graph = adj_matrix_graph.AdjacencyMatrixGraph()
    for i in range(1000):
        graph.add_vertex(f"V{i}")
    for i in range(999):
        graph.add_edge(f"V{i}", f"V{i+1}")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


@profile
def benchmark_lstgraph():
    start_time = time.time()

    graph = adj_list_graph.AdjacencyListGraph()
    for i in range(1000):
        graph.add_vertex(f"V{i}")
    for i in range(999):
        graph.add_edge(f"V{i}", f"V{i+1}")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    print("Deterministic test: 5 vertices and 5 edges (moderate connectivity) ")
    print(
        f"bench5v_adj_list total time: {timeit.timeit(bench5v5e_adj_list, number=10000)} seconds"
    )
    print(
        f"bench5v_adj_matrix total time: {timeit.timeit(bench5v5e_adj_matrix, number=10000)} seconds"
    )
    print("Profiling bench5v5e_adj_list:")
    cProfile.run("bench5v5e_adj_list(10000)")
    print("Profiling bench5v5e_adj_matrix:")
    cProfile.run("bench5v5e_adj_matrix(10000)")
    print("Deterministic test: 10 vertices fully connected")
    print(
        f"AdjacencyListGraph: {timeit.timeit(lambda: bench10v_fully_connected(adj_list_graph.AdjacencyListGraph), number=10000)} seconds"
    )
    print(
        f"AdjacencyMatrixGraph: {timeit.timeit(lambda: bench10v_fully_connected(adj_matrix_graph.AdjacencyMatrixGraph), number=10000)} seconds"
    )
    print("Profiling bench10v_fully_connected(AdjacencyListGraph)")
    cProfile.run(
        "[bench10v_fully_connected(adj_list_graph.AdjacencyListGraph) for _ in range(10000)]"
    )
    print("Profiling bench10v_fully_connected(AdjacencyMatrixGraph)")
    cProfile.run(
        "[bench10v_fully_connected(adj_matrix_graph.AdjacencyMatrixGraph) for _ in range(10000)]"
    )
    print("Space and time complexity adjacency list:")
    benchmark_lstgraph()
    print("Space and time complexity adjacency matrix: ")
    benchmark_mgraph()
