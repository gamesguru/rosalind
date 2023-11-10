#!/usr/bin/env python3

# query = "We tried list and we tried dicts also we tried Zen"
query = open("input/rosalind_ini6.txt", "r").read()
# print(query)

occurance_count_dict = {}

for word in query.split():
    if word not in occurance_count_dict:
        occurance_count_dict[word] = 1
    else:
        occurance_count_dict[word] += 1

for word, number_occurances in occurance_count_dict.items():
    print(word + " " + str(number_occurances))
