from simple_graph import Graph


class AdjacencyMatrixGraph(Graph):
    def __init__(self) -> None:
        self.vertex_to_index = {}  # vertex to index mapping
        self.index_to_vertex = {}  # index to vertex mapping
        self.adj_mtrx = []
        self.next_idx = 0

    def has_edge(self, u, v) -> bool:
        if (
            u in self.vertex_to_index
            and v in self.vertex_to_index
            and self.adj_mtrx[self.vertex_to_index[u]][self.vertex_to_index[v]] == 1
        ):
            return True
        return False

    def has_vertex(self, v) -> bool:
        if v in self.vertex_to_index:
            return True
        return False

    def add_edge(self, u, v) -> None:
        if self.has_vertex(u) and self.has_vertex(v):
            self.adj_mtrx[self.vertex_to_index[u]][self.vertex_to_index[v]] = 1

    def add_vertex(self, v) -> None:
        if v not in self.vertex_to_index:
            # update mapping of vertices to indices
            self.vertex_to_index[v] = self.next_idx
            self.index_to_vertex[self.next_idx] = v
            # update the next available integer label
            self.next_idx += 1
            # update adjacency matrix
            size = len(self.adj_mtrx)
            for row in self.adj_mtrx:
                row.append(0)  # Add a new column with 0s for the new vertex
            self.adj_mtrx.append([0] * (size + 1))  # Add a new row

    def get_vertices(self):
        return self.vertex_to_index.keys()

    def get_neighbors(self, v):
        is_neighbor = self.adj_mtrx[self.vertex_to_index[v]]
        neighbors = []
        for i in range(len(is_neighbor)):
            if is_neighbor[i] == 1:
                neighbors.append(self.index_to_vertex[i])
        return neighbors


if __name__ == "__main__":
    g = AdjacencyMatrixGraph()
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
    print(g.adj_mtrx)
    for vertex in g:
        print(vertex)
        print(g.get_neighbors(vertex))
