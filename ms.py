
def merge_sort(input):
    def merge(arr, l, m, r):

        s1 = m - l + 1
        s2 = r - m

        # Copy split data into two temp arrays
        L = arr[l:l + s1]
        R = arr[m + 1: m + 1 + s2]

        # Merge temp arrays back into arr[l..r]
        i = 0
        j = 0
        k = l
        while (i < s1 and j < s2):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements of L[]
        while i < s1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy any remaining elements of R[]
        while i < s2:
            arr[k] = R[j]
            j += 1
            k += 1

    lines = input.split('\n')
    # n = int(lines[0])
    arr = [int(x) for x in lines[1].split()]
    l = len(arr)

    n = 1
    while n < l:
        for i in range(0, l - 1, 2 * n):
            mid = min(i + n - 1, l - 1)
            j = min(i + 2 * n - 1, l - 1)
            # Pseudo in-place merge (uses log(n) auxillary space)
            merge(arr, i, mid, j)
        n *= 2

    # Print result
    print(arr)



merge_sort("""10
20 19 35 -18 17 -20 20 1 4 4""")

# with open('ms.txt') as ms:
#     merge(ms.read())
