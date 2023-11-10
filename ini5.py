#!/usr/bin/env python3

i = 0

with open("input/rosalind_ini5.txt", "r") as f:
    for line in f:
        i += 1
        if not i % 2:
            print(line.rstrip())
