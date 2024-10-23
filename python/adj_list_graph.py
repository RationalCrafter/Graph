from simple_graph import Graph
from singly_linked_list import SinglyLinkedList


class AdjacencyListGraph(Graph):
    """Implements an adjacency list representation
    of a graph as a dictionary of linked lists"""

    def __init__(self) -> None:
        self.adj_lst = {}

    def add_vertex(self, v) -> None:
        if v not in self.adj_lst:
            self.adj_lst[v] = SinglyLinkedList()

    # be careful with the undirected case, wherein u->v implies v->u!
    def add_edge(self, u, v) -> None:
        if u in self.adj_lst:
            if v not in self.adj_lst[u]:
                self.adj_lst[u].insert_front([v])

    def has_vertex(self, v) -> bool:
        return v in self.adj_lst

    def has_edge(self, u, v) -> bool:
        if u not in self.adj_lst or v not in self.adj_lst:
            # again be careful with the directed/undirected dichotomy
            return False
        else:
            return u in self.adj_lst and v in self.adj_lst[u]

    def get_vertices(self):
        return self.adj_lst.keys()

    def get_neighbors(self, v):
        return self.adj_lst[v]


if __name__ == "__main__":
    g = AdjacencyListGraph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(4, 2)
    g.add_edge(2, 5)
    g.add_edge(5, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(6, 6)
    print(g.adj_lst)
    for vertex in g:
        print(vertex)
