def sortedSquaredArray(array):
    # Write your code here.
    result = []
    for num in array:
        result.append(num ** 2)
        
    i = 0
    j = len(result) -1
    while (i <= j):
        if result[i] > result[j]:
            temp = result[i]
            result[i] = result[j]
            result[j] = temp
            j = j - 1
            i = 0
        elif result[i] == result[j] and i == j:
            i = i + 1
            j = len(result) -1
        else:
            j = j - 1

            
            
            
    return result
# arr = [-2, -1]
# arr = [-5, -4, -3, -2, -1]
# arr = [-7, -3, 1, 9, 22, 30]
arr = [-10, -5, 0, 5, 10]
print('Result ',sortedSquaredArray((arr)))