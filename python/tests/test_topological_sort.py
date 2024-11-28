import pytest
from topological_sort import topological_sort
from simple_graph_serializers import read_graph_from_json
from adj_list_graph import AdjacencyListGraph


@pytest.mark.parametrize(
    "input_graph_file,expected_output",
    [
        (
            "./tests/test_graphs/simple_dag.json",
            ["5", "4", "2", "3", "1"],
        ),  # Acceptable order
        (
            "./tests/test_graphs/simple_dag2.json",
            ["6", "5", "4", "2", "3", "1"],
        ),  # Acceptable order
    ],
)
def test_topological_sort(input_graph_file, expected_output):
    g = read_graph_from_json(input_graph_file, AdjacencyListGraph)

    result = topological_sort(g)

    # Ensure result respects the topological ordering (all dependencies are respected)
    for u in g:
        for v in g.get_neighbors(u):  # Check for each edge u -> v
            # Ensure that u appears before v in the sorted result
            assert result.index(u) < result.index(v), f"Failed for edge {u} -> {v}"

    # Check if result is a valid topological sort (we no longer compare exact order)
    assert set(result) == set(
        expected_output
    ), f"Result: {result}, Expected: {expected_output}"
