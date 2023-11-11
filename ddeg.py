#!/usr/bin/env python3

# input_data = """
# 5 4
# 1 2
# 2 3
# 4 3
# 2 4
# """

input_data = open("input/rosalind_ddeg.txt", "r").read().strip()

class Vertex:
    def __init__(self):
        """Create a lone vertex"""
        self.degree = 0
        self.adjacent_vertexes = set()

    def __str__(self):
        return f"Vertex(degree={self.degree}, adjacent_vertexes={self.adjacent_vertexes})"


class Graph:
    def __init__(self, n_vertexes, n_edges):
        """Create a new graph with specified # of vertexes"""
        self.expected_edges_num = n_edges

        self.vertexes = [Vertex() for x in range(n_vertexes)]
        self.edges = []

    def __str__(self):
        return f"Graph(n_vertexes={len(self.vertexes)}, n_edges={len(self.edges)})"

    def add_edge(self, id_vertex_from, id_vertex_to):
        # Append incoming AND outgoing, since is an undirected graph
        graph.edges.append((id_vertex_from, id_vertex_to))
        graph.edges.append((id_vertex_to, id_vertex_from))

        # Update degrees
        self.vertexes[id_vertex_from].degree += 1
        self.vertexes[id_vertex_to].degree += 1

        # Append adjacency list
        self.vertexes[id_vertex_from].adjacent_vertexes.add(id_vertex_to)
        self.vertexes[id_vertex_to].adjacent_vertexes.add(id_vertex_from)

    def double_degrees(self):
        degrees = ''
        for vertex in self.vertexes:
            print(vertex)
            # degree = vertex.degree
            degree = 0
            for _adj_vertex in vertex.adjacent_vertexes:
                degree += self.vertexes[_adj_vertex].degree
            degrees += f"{degree} "

        return degrees




for i, line in enumerate(input_data.strip().split("\n")):
    # Load vertexes tuple (first line is metadata)
    if i == 0:
        n_vertexes, n_edges = (int(x) for x in line.split())
        graph = Graph(n_vertexes, n_edges)
        print(graph)
        # vertex_degrees = list(0 for x in range(n_vertexes))
        continue

    # Store the edge in the graph
    id_vertex_from, id_vertex_to = (int(x) - 1 for x in line.split())
    print(f"{id_vertex_from} -> {id_vertex_to}")
    graph.add_edge(id_vertex_from, id_vertex_to)
    # vertex_degrees[id_vertex_from - 1] += 1
    # vertex_degrees[id_vertex_to - 1] += 1

# print(" ".join(str(x) for x in vertex_degrees))
print(graph)
print(graph.double_degrees())

