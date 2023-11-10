#!/usr/bin/env python3


# dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
dna = open('input/rosalind_ini.txt', "r").read().rstrip()

def _acgt():
    # NOTE: see their website for a more elegant solution
    occurance_dict = {'a': 0, 'c': 0, 'g': 0 , 't': 0}
    for _char in dna:
        occurance_dict[_char.lower()] += 1

    print(
        f"{occurance_dict['a']} {occurance_dict['c']} {occurance_dict['g']} {occurance_dict['t']}"
    )

_acgt()
