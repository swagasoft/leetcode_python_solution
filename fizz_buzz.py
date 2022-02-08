
def fizzbuzz(n):
    list2 = []

    for i in range(1, n + 1):
        print('see ', i)
        if i % 5 == 0 and i % 3 == 0:
            list2.append('FizzBuzz')
        elif i % 3 == 0:
            list2.append('Fizz')
        elif i % 5 == 0:
            list2.append('Buzz')
        else:
            list2.append(i)

    return list2


print(fizzbuzz(15))
