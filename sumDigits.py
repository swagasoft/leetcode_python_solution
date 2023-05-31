""" write a function that returns the sum of all of the digits in a given integer value """

def sumDigits(num: int):
 if(num == 0):
    return 0
 return (num % 10) + sumDigits(num // 10)


print('sum digits => ', sumDigits(560))