import pytest
import random

# from adj_list_graph import AdjacencyListGraph
from weighted_adj_list_graph import WeightedAdjacencyListGraph


# test basic vertex insertion
def test_10_vertex_insertion():
    g = WeightedAdjacencyListGraph()
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
    g = WeightedAdjacencyListGraph()
    for i in range(10000):
        g.add_vertex(i)
    # assert existence
    for i in range(10000):
        assert i in g


# test basic edge creation
def test_small_edge_set():
    g = WeightedAdjacencyListGraph()
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


# test weighted edge creation
def test_small_weighted_edge_set():
    g = WeightedAdjacencyListGraph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    # add edges
    g.add_edge("a", "b", weight=1.0)
    g.add_edge("b", "c", weight=2.0)
    # test edges
    assert g.has_edge("a", "b")
    assert g.has_edge("b", "c")
    assert not g.has_edge("a", "c")
    # test edge weights
    assert g.get_weight("a", "b") == 1.0
    assert g.get_weight("b", "c") == 2.0
    # alter edge weight and retest
    g.set_weight("a", "b", weight=2.5)
    g.set_weight("b", "c", weight=-2.0)
    # test new edge weights
    assert g.get_weight("a", "b") == 2.5
    assert g.get_weight("b", "c") == -2.0


# test graph creation with fully connected small graph
def test_fully_connected_10v_creation():
    g = WeightedAdjacencyListGraph()
    # add vertices
    for i in range(10):
        g.add_vertex(i)
    # assert vertex existence
    for i in range(10):
        assert g.has_vertex(i)
    random.seed(0)  # for repeatability
    test_weights = {}
    # add edges
    for i in range(10):
        for j in range(10):
            # generate some random weight for each edge
            weight = random.random()
            g.add_edge(i, j, weight)
            test_weights[(i, j)] = weight
    # test edge existence
    for i in range(10):
        for j in range(10):
            assert g.has_edge(i, j) is True
            # test if the edge weight was correctly stored
            assert g.get_weight(i, j) == test_weights[(i, j)]
    # test nonexistent edges
    for i in range(10, 20):
        for j in range(10, 20):
            assert g.has_edge(i, j) is False
            assert g.get_weight(i, j) is None
            # the following should raise exceptions for no weight is allowed in nonexistent edges
            with pytest.raises(ValueError):
                g.set_weight(i, j, random.random())
