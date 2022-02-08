class solution:
    def squareEven(arr: list):
        for i in range(len(arr)):

            if i % 2 == 0:
                arr[i] = arr[i] ** 2

        return arr

    val = [9, -2, -9, 11, 56, -12, -3]
    print(squareEven(val))
