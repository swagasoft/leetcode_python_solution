
def isPrimeNumber(num: int) -> None:
    result = False

    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                print(num, ' is not a prime number')
                return
        print(num ,' is a prime number')

    else:

        print(num, ' is not a prime number')



print(isPrimeNumber(3))