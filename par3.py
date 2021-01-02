def par(input):
    a = [int(x) for x in input.split("\n")[1].split()]
    n = len(a)
    a0 = a[0]
    print(a)

    l = 1
    r = n - 1
    while l < r:
        for i in range(l, n):
            if a[i] > a0:
                l = i
                break
        for j in range(r, 0, -1):
            if a[j] <= a0:
                r = j
                break
        if l < r:
            a[l], a[r] = a[r], a[l]
        else:
            # swap pivot
            a[0], a[r] = a[r], a[0]
            break

    l = 1
    r = r
    while l < r:
        for j in range(r, l - 1, -1):
            if a[j] != a0:
                r = j
                break
        for i in range(l, r + 1):
            if a[i] == a0:
                l = i
                break
        if l < r:
            a[l], a[r] = a[r], a[l]
        else:
            # exit
            break

    print(a)


# par(
#     """9
# 4 5 6 4 1 2 5 7 4"""
# )

with open("/home/shane/Downloads/rosalind_par3.txt") as f:
    par(f.read())
