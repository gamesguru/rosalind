def maj(input):
    def maj_e(arr):
        c = len(arr) // 2

        occ = {}
        for e in arr:
            if e in occ:
                occ[e] += 1
            else:
                occ[e] = 1
            if occ[e] > c:
                return e
        return -1

    lines = input.split("\n")
    # k = int(lines[0].split()[0])
    # n = int(lines[0].split()[1])

    arrs = [[int(x) for x in arr.split()] for arr in lines[1:]]

    result = [str(maj_e(arr)) for arr in arrs]
    print(" ".join(result))
    return result


maj(
    """4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1"""
)
