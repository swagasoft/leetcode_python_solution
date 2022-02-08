
def isPalindrome(n):
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    reverseNum = 0
    while (n > reverseNum):
        pop = n % 10
        reverseNum = reverseNum * 10 + pop
        n = n / 10
    return n == reverseNum or n == reverseNum / 10


num = 12321
print(isPalindrome(num))
