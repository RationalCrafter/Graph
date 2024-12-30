from simple_weighted_graph import WeightedGraph
from adj_list_graph import AdjacencyListGraph


class WeightedAdjacencyListGraph(WeightedGraph, AdjacencyListGraph):
    """A weighted adjacency list graph."""

    def __init__(self) -> None:
        super().__init__()
        self.weights = {}  # Dictionary to store edge weights as (u,v) -> weight

    def add_edge(self, u, v, weight=None, undirected=False) -> None:
        # Add the edge to the adjacency list first
        AdjacencyListGraph.add_edge(self, u, v, undirected)
        # Then set the weight for the edge
        if weight is not None:
            self.set_weight(u, v, weight, undirected)

    def get_weight(self, origin_vertex, destination_vertex) -> float:
        """Return the weight of the edge from u to v. Returns None if no edge exists."""
        return self.weights.get((origin_vertex, destination_vertex), None)

    def set_weight(
        self, origin_vertex, destination_vertex, weight, undirected=False
    ) -> None:
        """Set the weight of the edge from u to v."""
        if self.has_edge(origin_vertex, destination_vertex):
            self.weights[(origin_vertex, destination_vertex)] = weight
            if (
                origin_vertex != destination_vertex
                and undirected
                and (destination_vertex, origin_vertex) not in self.weights
            ):  # For undirected graphs, store the reverse edge weight
                self.weights[(destination_vertex, origin_vertex)] = weight
        else:
            raise ValueError(
                f"Cannot set weight: no edge exists between {origin_vertex} and {destination_vertex}."
            )


if __name__ == "__main__":
    g = WeightedAdjacencyListGraph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 5)
    print(g.get_weight("A", "B"))
    print(g.get_weight("B", "C"))
    print(g.set_weight("A", "B", -1))
    print(g.get_weight("A", "B"))
    try:
        print(g.set_weight("A", "Z", 3.14159))  # this should fail
    except ValueError as e:
        print(e)
    # test type system
    g2 = AdjacencyListGraph()
    g2.add_vertex(1)
    g2.add_vertex(2)
    g2.add_vertex(3)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print(type(g))
    print(type(g2))
    print(f"are they of the same type? {type(g)==type(g2)}")
    print(isinstance(g, AdjacencyListGraph))
    print(isinstance(g2, AdjacencyListGraph))
    print(isinstance(g, WeightedAdjacencyListGraph))
    print(isinstance(g2, WeightedAdjacencyListGraph))
