from simple_graph import Graph


class WeightedGraph(Graph):
    """WeightedGraph base class"""

    def get_weight(self, origin_vertex, destination_vertex):
        raise NotImplementedError

    def set_weight(self, origin_vertex, destination_vertex, weight):
        raise NotImplementedError
