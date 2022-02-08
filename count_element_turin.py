
def countelement(arr: list):
    result = 0
    ls = []
    arr.sort()
    print(arr)
    print(type(arr))
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] != 0:

                if(arr[j] + 1) == arr[i]:
                    result = arr[i]

    return result


# data = [1, 2, 3]
# data = [1, 1, 2]
data = [1, 3, 2, 3, 5, 0]
print(countelement(data))
