#!/usr/bin/env python3

import os

_file = "input/rosalind_bfs.txt"

if os.path.isfile(_file):
    input_data = open(_file, "r").read().strip()
else:
    input_data = []

input_data = (
    input_data
    or """
6 6
4 6
6 5
4 3
3 5
2 1
1 4
"""
)


class Vertex:
    def __init__(self, id):
        """Create a lone vertex"""
        self.id = id
        self.edges = []

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, edges={self.edges})"


class GraphDirected:
    def __init__(self, n_vertexes, n_edges):
        """Create a new graph with specified # of vertexes"""
        self.expected_edges_num = n_edges

        self.vertexes = [Vertex(x) for x in range(n_vertexes)]
        # self.edges = []

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            + f"(n_vertexes={len(self.vertexes)}, "
            + f"n_edges={sum(len(x.edges) for x in self.vertexes)})"
        )

    def add_edge(self, id_vertex_from, id_vertex_to):
        # Add edge: "incoming --> outbound" vertex
        graph.vertexes[id_vertex_from].edges.append(id_vertex_to)

    def shortest_paths(self, vertex_id_origin):
        distances = {x.id: -1 for x in self.vertexes}
        distances[vertex_id_origin] = 0
        print(" ".join(str(x) for x in distances.values()))

        distance = 0
        # NOTE: 1 -> 0, the array index is "zero" but the graph starts with "vertex 1"
        vertex = self.vertexes[vertex_id_origin]
        print(vertex)
        print()

        visited = {vertex.id}
        queue = vertex.edges
        queued = []
        while queue or queued:
            distance += 1
            queue.extend(set(queued))
            queued.clear()
            for edge in queue:
                if edge not in visited:
                    if distances[edge] == -1:
                        distances[edge] = distance
                    elif distance < distances[edge]:
                        distances[edge] = distance
                    visited.add(edge)
                    queued.extend(self.vertexes[edge].edges)
            queue.clear()

        # Print end result
        print(" ".join(str(x) for x in distances.values()))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main logic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i, line in enumerate(input_data.strip().split("\n")):

    # Initialize graph with n_vertexes
    if i == 0:
        n_vertexes, n_edges = (int(x) for x in line.split())
        graph = GraphDirected(n_vertexes, n_edges)
        print(graph)

        # First line is metadata, continue
        continue

    # Store the edges on the graph
    id_vertex_from, id_vertex_to = (int(x) - 1 for x in line.split())

    # print(f"{id_vertex_from} -> {id_vertex_to}")
    graph.add_edge(id_vertex_from, id_vertex_to)

for vertex in graph.vertexes:
    print(vertex)
    print(vertex.edges)
print(graph)
graph.shortest_paths(vertex_id_origin=0)
