import json
from simple_graph import Graph
from adj_list_graph import AdjacencyListGraph


def save_graph_to_json(graph: Graph, filename: str):
    """Saves the graph to a json file named 'filename.json'."""
    data = {
        "vertices": [*graph.get_vertices()],
        "edges": {v: graph.get_neighbors(v) for v in graph},
    }
    with open(filename, "w+") as json_file:
        json.dump(data, json_file)


def read_graph_from_json(filename: str, graph_type) -> Graph:
    """Reads a graph serialized as json to 'filename.json' into a variable
    of type graph_type. This function might throw an exception since it relies of file I/O with 'filename.json' which may not exist.
    """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        g = graph_type()
        for v in data["vertices"]:
            g.add_vertex(v)
        #            print(v)
        #        print(data["edges"])
        for u in data["edges"]:
            for v in data["edges"][u]:
                g.add_edge(u, v)
    return g


if __name__ == "__main__":
    # g = AdjacencyListGraph()
    # g.add_vertex("a")
    # g.add_vertex("b")
    # g.add_vertex("c")
    # g.add_edge("a", "b")
    # g.add_edge("b", "c")
    # g.add_edge("c", "a")
    # print(g)
    # print(*g.get_vertices())
    # save_graph_to_json(g, "test_graph.json")
    # print("Reading saved data...")
    # new_g = read_graph_from_json("test_graph.json", AdjacencyListGraph)
    # print(new_g.get_vertices())
    # print(new_g.get_neighbors("a"))
    final_g = read_graph_from_json(
        "tests//test_graphs//hundred_node_graph.json", AdjacencyListGraph
    )
    print(final_g)
