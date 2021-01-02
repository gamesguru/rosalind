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

    # l = 1
    # while l < r:
    #     for i in range(l, r):
    #         if a[i]

    print(a)


par(
    """9
4 5 6 4 1 2 5 7 4"""
)
