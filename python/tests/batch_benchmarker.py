from adj_list_graph import AdjacencyListGraph
from adj_matrix_graph import AdjacencyMatrixGraph
from simple_graph_serializers import read_graph_from_json
import pytest


if __name__ == "__main__":
    g1 = AdjacencyListGraph()
    g2 = AdjacencyMatrixGraph()
    print(g1)
    print(g2)
