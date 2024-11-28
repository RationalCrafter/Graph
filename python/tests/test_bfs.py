import pytest
import adj_list_graph
import bfs


def test_bfs_linear_graph():
    g = adj_list_graph.AdjacencyListGraph()
    expected_distance = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    expected_predecessor = {1: None, 2: 1, 3: 2, 4: 3, 5: 4}
    for i in range(1, 6):
        g.add_vertex(i)
    for i in range(2, 6):
        g.add_edge(i - 1, i)
    distance, predecessor = bfs.bfs(g, 1)
    assert expected_predecessor == predecessor
    assert expected_distance == distance
