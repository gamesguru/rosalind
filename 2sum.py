#!/usr/bin/env python3

import math

# input_data = """
# 4 5
# 2 -3 4 10 5
# 8 2 4 -2 -8
# -5 2 3 2 -4
# 5 4 -5 6 8
# """

input_data = open("input/rosalind_2sum.txt", "r").read().strip()

def get_2sum():

    def process_line():
        for i, item in enumerate(line.split()):
            item = int(item)
            if -item in items.keys():
                # print(f"{item}@{i} & {-item}@{items[-item]}")
                print(f"{i + 1} {items[-item] + 1}")
                return True
        print(-1)

    for i, line in enumerate(input_data.strip().split("\n")):
        # Load values n and k (first line is metadata)
        if i == 0:
            k, n = (int(x) for x in line.split())
            continue

        items = {int(x): i for i, x in enumerate(line.split())}
        # print(items.items())
        process_line()


get_2sum()
