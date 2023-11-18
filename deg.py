#!/usr/bin/env python3

# input_data = """
# 6 7
# 1 2
# 2 3
# 6 3
# 5 6
# 2 5
# 2 4
# 4 1
# """

input_data = open("input/rosalind_deg.txt", "r").read().strip()


for i, line in enumerate(input_data.strip().split("\n")):
    # Load vertexes tuple (first line is metadata)
    if i == 0:
        n_vertexes, n_edges = (int(x) for x in line.split())
        vertex_degrees = list(0 for x in range(n_vertexes))
        print(vertex_degrees)
        continue

    # Store the edge in the graph
    id_vertex_from, id_vertex_to = (int(x) for x in line.split())
    print(f"{id_vertex_from} -> {id_vertex_to}")
    vertex_degrees[id_vertex_from - 1] += 1
    vertex_degrees[id_vertex_to - 1] += 1

print(" ".join(str(x) for x in vertex_degrees))
