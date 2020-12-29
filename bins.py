def bin(input):
    def index(e, A, p=None, q=None):
        if p is None or q is None:
            p = 0
            q = len(A) - 1

        if p == q:
            if A[p] == e:
                return p
            else:
                return -1
        else:
            i = (p + q) // 2
            if e < A[i]:
                return index(e, A, p=p, q=(i - 1))
            elif e > A[i]:
                return index(e, A, p=(i + 1), q=q)
            else:
                return i

    lines = input.split("\n")
    n = int(lines[0])
    m = int(lines[1])

    sa = [int(x) for x in lines[2].split()]
    ua = [int(x) for x in lines[3].split()]

    result = [index(x, sa) for x in ua]
    print(result)
    return result


bin(
    """5
6
10 20 30 40 50
40 10 35 15 40 20"""
)

