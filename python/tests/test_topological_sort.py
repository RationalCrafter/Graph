import pytest
from topological_sort import topological_sort
from simple_graph_serializers import read_graph_from_json
from adj_list_graph import AdjacencyListGraph


@pytest.mark.parametrize(
    "input_graph_file,expected_output",
    [
        ("./tests/test_graphs/simple_dag.json", ["4", "5", "2", "3", "1"]),
        ("./tests/test_graphs/simple_dag2.json", ["4", "5", "6", "2", "3", "1"]),
    ],
)
def test_topological_sort(input_graph_file, expected_output):
    g = read_graph_from_json(input_graph_file, AdjacencyListGraph)
    assert topological_sort(g) == expected_output
