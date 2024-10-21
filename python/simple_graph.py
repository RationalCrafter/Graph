"""Implementation of a graph using an adjacency list. 
Core operations:
    1.Insertion:
        -Add a vertex
        -Add an edge
    2. Membership testing:
        -Check if a vertex exists
        -Check if an edge exists between 2 vertices."""


class Graph:
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
