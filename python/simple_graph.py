"""Declaration of a simple graph base class. 
Core operations:
    1.Insertion:
        -Add a vertex
        -Add an edge
    2. Membership testing:
        -Check if a vertex exists
        -Check if an edge exists between 2 vertices.
    3. Extra functionality:
        -Get the set of vertices in the graph
        -Get the neighbors of a given vertex in the graph."""


class Graph:
    """Graph base class"""

    def __init__(self) -> None:
        raise NotImplementedError

    def add_vertex(self, v) -> None:
        raise NotImplementedError

    def add_edge(self, u, v) -> None:
        raise NotImplementedError

    def has_vertex(self, v) -> bool:
        raise NotImplementedError

    def has_edge(self, u, v) -> bool:
        raise NotImplementedError

    def get_vertices(self):
        return NotImplementedError

    def __iter__(self):
        """This method should return an iterator over the graph's vertices."""
        return iter(self.get_vertices())

    def get_neighbors(self, v):
        """Return the neighbors of v.
        Specific to each graph representation."""
        raise NotImplementedError
