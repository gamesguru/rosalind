def bin(input):
    def index(e, A):
        p = 0
        q = len(A) - 1

        while q > p:
            i = (p + q) // 2
            if e == A[i]:
                return i + 1
            elif e < A[i]:
                p = p
                q = i - 1
            else:
                p = i + 1
                q = q

        if A[p] == e:
            return p + 1
        return -1

    lines = input.split("\n")
    # n = int(lines[0])
    # m = int(lines[1])

    sa = [int(x) for x in lines[2].split()]
    ua = [int(x) for x in lines[3].split()]

    result = [index(x, sa) for x in ua]
    print(" ".join(str(x) for x in result))
    return result


bin(
    """5
6
10 20 30 40 50
40 10 35 15 40 20"""
)
