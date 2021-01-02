def par(input):
    a = [int(x) for x in input.split("\n")[1].split()]
    n = len(a)
    a0 = a[0]
    print(a0)

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
        l_old = l
        for i in range(l, r + 1):
            if a[i] == a0:
                l = i
                break
        if l == l_old:
            break
        elif l < r:
            a[l], a[r] = a[r], a[l]
        else:
            # exit
            break

    print(" ".join(str(x) for x in a))


# par(
#     """9
# 4 5 6 4 1 2 5 7 4"""
# )

# par(
#     """10
# 7 25 77 -56 -32 7 -6 39 84 45 -51 71 58 75 25 -80 39 -5 -16 -74 -74 95 -50 7 -57 -13 -49 -52 -73 78 62 -95 -68 -88 23 60 28 -20 -82 64 98 72 93 -90 -20 20 -63 68 84 -78 72 -22 21 81 37 79 40 -79 78 -6 85 -3 -33 -14 93 -35 -29 -52 -25 -98 -56 -26 96 -41 47 -93 -45 -33 70 50 8 -18 3 73 1 -2 43 98 -61 53 32 -64 -34 -3 -16 -56 -75 3 86 29
# """
# )

with open("/home/shane/Downloads/rosalind_par3.txt") as f:
    par(f.read())
