import pytest
from adj_matrix_graph import AdjacencyMatrixGraph


# test basic vertex insertion
def test_10_vertex_insertion():
    g = AdjacencyMatrixGraph()
    for i in range(10):
        g.add_vertex(i)
    # assert existence
    for i in range(10):
        # doesn't directly require overloading
        assert g.has_vertex(i) is True
        # uses __contains__
        assert i in g


# test basic vertex insertion with large vertex set
def test_10000_vertex_insertion():
    g = AdjacencyMatrixGraph()
    for i in range(10000):
        g.add_vertex(i)
    # assert existence
    for i in range(10000):
        assert i in g


# test basic edge creation
def test_small_edge_set():
    g = AdjacencyMatrixGraph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    # add edges
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    # test edges
    assert g.has_edge("a", "b")
    assert g.has_edge("b", "c")
    assert not g.has_edge("a", "c")


# test graph creation with fully connected small graph
def test_fully_connected_10v_creation():
    g = AdjacencyMatrixGraph()
    # add vertices
    for i in range(10):
        g.add_vertex(i)
    # assert vertex existence
    for i in range(10):
        assert g.has_vertex(i)
    # add edges
    for i in range(10):
        for j in range(10):
            g.add_edge(i, j)
    # test edge existence
    for i in range(10):
        for j in range(10):
            assert g.has_edge(i, j) is True
    # test nonexistent edges
    for i in range(10, 20):
        for j in range(10, 20):
            assert g.has_edge(i, j) is False
