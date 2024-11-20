"""A simple script to assist with user input of graphs.
The goal is to provide a quick and practical way to describe
graphs and generate simple and easily exchangeable text file
representations of them"""

from simple_graph_serializers import save_graph_to_json
from adj_list_graph import AdjacencyListGraph

if __name__ == "__main__":
    print("store_graph: ")
    filename = input("File name: ")
    print(
        "By default the file will be written in JSON."
    )  # add option for other formats later

    g = AdjacencyListGraph()
    print("Vertex Input: ")
    is_finished = False
    while not is_finished:
        v = input("Insert a vertex name: ")
        g.add_vertex(v)
        go_on = input("Are there more vertices(Y/n)? ").strip().lower()
        is_finished = go_on == "n"
    is_finished = False
    print("Edge input:")
    while not is_finished:
        e = input("Insert an edge: ")
        t = e.split(" ")
        if len(t) != 2:
            print("Error: must provide 2 vertices")
        g.add_edge(t[0], t[1])
        go_on = input("Are there more edges(Y/n)? ").strip().lower()
        is_finished = go_on == "n"
    save_graph_to_json(g, filename + ".json")
