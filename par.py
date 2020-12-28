def par(arr):
    a = [int(x) for x in arr.split()]
    n = len(a)
    a0 = a[0]
    # TODO: resolve quadratic running time!
    while True:
        for i in range(1, n):
            if a[i] >= a0:
                l = i
                break
        for j in range(n - 1, 0, -1):
            if a[j] < a0:
                r = j
                break
        if l < j:
            a[i], a[j] = a[j], a[i]
        else:
            # Swap pivot
            a[0] , a[j] = a[j], a[0]
            break
    print(' '.join(str(x) for x in a))

par("7 2 5 6 1 3 9 4 8")
# par("7 9 2 5 8 1 3 4 6")
# par("")
