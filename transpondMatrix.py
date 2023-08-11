def transposeMatrix(matrix):
    # Write your code here.

    row = len(matrix)
    col =  len(matrix[0])
    result = [[0] * row for  x in range(col)] 
    print("result ", result)
    
    for i in range(row):
        for j in range(col):
            result[j][i] = matrix[i][j]
    
    return result

matrix =  [[1,2],[3,4],[5,6]]
print("result2 ", transposeMatrix(matrix))

