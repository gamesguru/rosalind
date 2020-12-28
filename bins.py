
def bin(input):

    def index(e, a):
        n = len(a)
        # k = 1
        # i = n // 2 ** k

        p = 1
        q = n
        while : # i > 0:
            if e < a[i]:
                k += 1
                i = n // 2 ** k
            elif e > a[i]:
                k += 1
                i = n // 2 ** k
            else:
                return i

    lines = input.split('\n')
    n = int(lines[0])
    m = int(lines[1])

    sa = [int(x) for x in lines[2].split()]
    ua = [int(x) for x in lines[3].split()]

    return [index(x, sa) for x in ua]

bin("""5
6
10 20 30 40 50
40 10 35 15 40 20""")

