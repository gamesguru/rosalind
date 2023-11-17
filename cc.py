#!/usr/bin/env python3
"""
The task is to use depth-first search to compute the number of
connected components in a given undirected graph.
"""

import os

_FILE = "input/rosalind_cc.txt"

if os.path.isfile(_FILE):
    with open(_FILE, "r", encoding="utf-8") as _f:
        INPUT_DATA = _f.read().strip()
else:
    INPUT_DATA = str()

INPUT_DATA = (
    INPUT_DATA
    or """
12 13
1 2
1 5
5 9
5 10
9 10
3 4
3 7
3 8
4 8
7 11
8 11
11 12
8 12
"""
)


class Vertex:
    """Create a lone vertex"""

    def __init__(self, id):
        self.id = id
        self.edges = []

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, edges={self.edges})"


class GraphUnDirected:
    """Create a new graph with specified # of vertexes"""

    def __init__(self, n_vertexes, n_edges):
        self.expected_edges_num = n_edges * 2  # double for undirected graphs

        self.vertexes = [Vertex(x) for x in range(n_vertexes)]

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            + f"(n_vertexes={len(self.vertexes)}, "
            + f"n_edges={sum(len(x.edges) for x in self.vertexes)})"
        )

    def add_edge(self, id_vertex_from, id_vertex_to):
        """Add edge: "incoming --> outbound" vertex"""
        self.vertexes[id_vertex_from].edges.append(id_vertex_to)
        # undirected graph, so add both ways
        self.vertexes[id_vertex_to].edges.append(id_vertex_from)

    def validate_edge_number(self):
        """Check the edge number meets expected/given value"""
        expected = self.expected_edges_num
        actual = sum(len(x.edges) for x in self.vertexes)
        if actual != expected:
            raise ValueError(
                f"Wrong number of edges: expected {expected}, actual {actual}"
            )

    def connected_components(self, current_node: int):
        """The main algorithm"""

        queue = [current_node]
        explored = set(queue)

        while queue:
            print(f"Current Node: {queue[0]}")
            vertex = self.vertexes[queue[0]]
            for edge in vertex.edges:
                if edge not in explored:
                    queue.append(edge)
                    explored.add(edge)
            queue.pop(0)

        current_node = max(explored)
        return explored


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Read input (into graph)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():
    """The main program"""

    for i, line in enumerate(INPUT_DATA.strip().split("\n")):

        # Initialize graph with n_vertexes
        if i == 0:
            n_vertexes, n_edges = (int(x) for x in line.split())
            graph = GraphUnDirected(n_vertexes, n_edges)
            print(graph)

            # First line is metadata, continue
            continue

        # Store the edges on the graph
        id_vertex_from, id_vertex_to = (int(x) - 1 for x in line.split())

        # print(f"{id_vertex_from} -> {id_vertex_to}")
        graph.add_edge(id_vertex_from, id_vertex_to)

    # Validate edge number
    graph.validate_edge_number()

    # Print graph info
    for vertex in graph.vertexes:
        print(vertex)
    print(graph)

    # Run algorithm
    print()
    print("Running main algorithm...")
    print()
    segments = []
    explored = set()
    target = set(x.id for x in graph.vertexes)

    while target.difference(explored):
        current_node = min(target.difference(explored))

        segment = graph.connected_components(current_node=current_node)
        print(f"segment:  {segment}")
        segments.append(segment)
        explored = explored.union(segment)
        print(f"explored: {explored}")
        print()

    # Print number of segments, only output for this algorithm / problem
    print(f"Answer: {len(segments)}")


if __name__ == "__main__":
    # Run the main program
    main()
