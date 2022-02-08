
def trailingZero(n):
    count = 0
    while (n > 0):
        n = n / 5
        count += n
    return count


print(trailingZero(128))
