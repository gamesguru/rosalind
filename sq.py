#!/usr/bin/env python3
"""
The task is to use depth-first search to compute the number of
connected components in a given undirected graph.
"""

import os

_cur_module = os.path.basename(__file__).split(".")[0]

_FILE = f"input/rosalind_{_cur_module}.txt"

if os.path.isfile(_FILE):
    with open(_FILE, "r", encoding="utf-8") as _f:
        INPUT_DATA = _f.read().strip()
else:
    INPUT_DATA = str()

INPUT_DATA = (
    INPUT_DATA
    or """
2

4 5
3 4
4 2
3 2
3 1
1 2

4 4
1 2
3 4
2 4
4 1
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

    def square_cycle(self) -> bool:
        """
        Check if a given graph contains a non-intersecting square cycle.
        This time, I'll use a recursive instead of iterative method.
        """

        def loopback(n: int, vertex: Vertex, paths: list) -> tuple[int, list]:
            """Recursive call"""

            return n, paths

        # Use a depth first search to look for cycles (naive, no dynamic programming)
        paths = []

        vertex = self.vertexes[0]
        queue = [vertex.edges]
        for vertex in self.vertexes:
            n, paths = loopback(n=n, vertex=vertex, paths=paths)
            # for edge in vertex.edges:
            #     paths = []

            # for i in range(4):

        return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Read input (into graph)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():
    """The main program"""

    _raw_data = INPUT_DATA.strip().split("\n\n")
    n_graphs = int(_raw_data.pop(0))

    # Validate graph number
    if n_graphs != len(_raw_data):
        raise ValueError(f"Expected {n_graphs} graphs, got {len(_raw_data)}")

    # Read in each graph
    for _graph_input in _raw_data:
        # Read in each edge (and first line of edge-list format is metadata)
        for i, line in enumerate(_graph_input.strip().split("\n")):

            # Initialize graph with n_vertexes
            if i == 0:
                n_vertexes, n_edges = (int(x) for x in line.split())
                graph = GraphUnDirected(n_vertexes, n_edges)
                # print(graph)

                # First line is metadata, continue
                continue

            # Store the edges on the graph
            id_vertex_from, id_vertex_to = (int(x) - 1 for x in line.split())

            # print(f"{id_vertex_from} -> {id_vertex_to}")
            graph.add_edge(id_vertex_from, id_vertex_to)

        # Validate edge number
        graph.validate_edge_number()

        # Run algorithm
        result = "1" if graph.square_cycle() else "-1"
        print(result, end=" ")

    # Finished
    print()


if __name__ == "__main__":
    # Run the main program
    main()
