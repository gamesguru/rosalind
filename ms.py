
def merge_sort(input):
    def merge(p, i, q):
        pass

    lines = input.split('\n')
    n = int(lines[0])
    arr = [int(x) for x in lines[1].split()]

    curr_size = 1
    left_start = 0


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
