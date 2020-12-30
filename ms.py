
def merge_sort(input):
    def merge(a, b):
        c = []
        while a or b:
            if not b:
                c.append(a.pop(0))
            elif not a:
                c.append(b.pop(0))
            elif a[0] < b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        return c

    lines = input.split('\n')
    # n = int(lines[0])
    arr = [int(x) for x in lines[1].split()]
    l = len(arr)

    n = 1
    while n < l:
        for i in range(0, l - 1, 2 * n):
            mid = min(i + n - 1, l - 1)
            j = min(i + 2 * n - 1, l - 1)
            merge(arr, i, mid, j)
        n *= 2
    # i = n // 2
    # result = merge(arr[:i], arr[i:])
    # print(result)

    # curr_size = 1
    # left_start = 0




    # i = n // 2
    # arr1 = arr[0:i]
    # arr2 = arr[i:n]

    # # TODO: implement custom sort method :)
    # arr1 = sort(arr1)
    # arr2 = sort(arr2)



merge_sort("""10
20 19 35 -18 17 -20 20 1 4 4""")

# with open('ms.txt') as ms:
#     merge(ms.read())
