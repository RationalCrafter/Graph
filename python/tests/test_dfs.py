import pytest
import adj_list_graph
import dfs


def test_dfs_with_back_edges():
    # Create the graph and add vertices
    g = adj_list_graph.AdjacencyListGraph()
    for i in range(1, 5):
        g.add_vertex(i)

    # Add edges to form a graph with a back edge: 1 -> 2 -> 3 -> 4, and 4 -> 2 (back edge)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 2)  # Back edge

    # Expected results
    expected_predecessor = {1: None, 2: 1, 3: 2, 4: 3}
    expected_discovery = {1: 1, 2: 2, 3: 3, 4: 4}
    expected_finalization = {1: 8, 2: 7, 3: 6, 4: 5}
    expected_back_edges = {4: 2}  # 4 -> 2 is the back edge

    # Perform DFS with back edge detection enabled
    predecessor, discovery, finalization, back_edges = dfs.dfs(
        g, detect_back_edges=True
    )

    # Assert that the DFS results match the expected dictionaries
    assert expected_predecessor == predecessor
    assert expected_discovery == discovery
    assert expected_finalization == finalization
    assert expected_back_edges == back_edges
