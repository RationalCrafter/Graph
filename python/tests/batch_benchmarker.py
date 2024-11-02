from adj_list_graph import AdjacencyListGraph
from adj_matrix_graph import AdjacencyMatrixGraph
from simple_graph_serializers import read_graph_from_json
from bfs import bfs
from dfs import dfs
import time
import csv
import random


def benchmark_graph_representation(
    input_files, graph_classes, number_repetitions=10000
):
    result_file = open("batch.log", "w+")
    for input_filename in input_files:
        result_file.write(f"\nbuild time test on {input_filename}:")
        for graph_type in graph_classes:
            start_time = time.time()
            g = None
            for _ in range(number_repetitions):
                g = read_graph_from_json(input_filename, graph_type)
            end_time = time.time()
            result_file.write(
                f"\n{graph_type}: average time was {(end_time-start_time)/number_repetitions}s"
            )
        result_file.write(f"\nhas_edge time test on {input_filename}: ")
        for graph_type in graph_classes:
            g = read_graph_from_json(input_filename, graph_type)
            vertices = list(g.get_vertices())
            start_time = time.time()
            for _ in range(number_repetitions):
                # time graph edge existence testing
                g.has_edge(random.choice(vertices), random.choice(vertices))
            end_time = time.time()
            result_file.write(
                f"\n{graph_type}: has_edge {(end_time-start_time)/number_repetitions}s"
            )
        result_file.write(f"\nhas_vertex time test on {input_filename}: ")
        for graph_type in graph_classes:
            g = read_graph_from_json(input_filename, graph_type)
            vertices = list(g.get_vertices())
            start_time = time.time()
            for _ in range(number_repetitions):
                g.has_vertex(random.choice(vertices))
            end_time = time.time()

            result_file.write(
                f"\n{graph_type}: has_vertex {(end_time-start_time)/number_repetitions}s"
            )
        result_file.write("\n\n")
    result_file.close()


def benchmark_bfs(input_files, graph_classes, number_repetitions=1000):
    result_file = open("batch_bfs.log", "w")
    for input_filename in input_files:
        result_file.write(f"\ntraversal time on {input_filename}")
        for graph_type in graph_classes:
            g = read_graph_from_json(input_filename, graph_type)
            # pick a source ...
            vertices = list(g.get_vertices())
            source = vertices[0]
            start_time = time.time()
            for _ in range(number_repetitions):
                bfs(g, source)
            end_time = time.time()
            result_file.write(
                f"\nBFS on {graph_type}: {(end_time-start_time)/number_repetitions}"
            )
    result_file.close()


def benchmark_dfs(input_files, graph_classes, number_repetitions=1000):
    result_file = open("batch_dfs.log", "w")
    for input_filename in input_files:
        result_file.write(f"\ntraversal time on {input_filename}")
        for graph_type in graph_classes:
            g = read_graph_from_json(input_filename, graph_type)
            start_time = time.time()
            for _ in range(number_repetitions):
                dfs(g)
            end_time = time.time()
            result_file.write(
                f"\nDFS on {graph_type}: {(end_time-start_time)/number_repetitions}"
            )
    result_file.close()


if __name__ == "__main__":

    test_inputs = [
        "./tests/test_graphs/bfs_vs_dfs_tester_graph.json",
        "./tests/test_graphs/cycle_with_floats.json",
        "./tests/test_graphs/hundred_node_graph.json",
        "./tests/test_graphs/simple_graph.json",
        "./tests/test_graphs/sparse_graph_mixed_types.json",
        "./tests/test_graphs/star_graph.json",
    ]
    benchmark_graph_representation(
        test_inputs,
        [AdjacencyListGraph, AdjacencyMatrixGraph],
    )

    benchmark_bfs(test_inputs, [AdjacencyListGraph, AdjacencyMatrixGraph])
    benchmark_dfs(test_inputs, [AdjacencyListGraph, AdjacencyMatrixGraph])
