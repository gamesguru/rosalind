def med(input):
    a = [int(x) for x in input.split("\n")[1].split()]
    a.sort()
    k = int(input.split("\n")[2])

    # print(" ".join(str(x) for x in result))
    print(a[k - 1])


# med(
#     """11
# 2 36 5 21 8 13 11 20 5 4 1
# 8"""
# )

with open("/home/shane/Downloads/rosalind_med.txt") as f:
    med(f.read())
