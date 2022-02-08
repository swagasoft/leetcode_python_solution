
def reverse_string(str: list):
    left = 0
    right = len(str) - 1

    while (left < right):
        tmp = str[left]
        str[left] = str[right]
        str[right] = tmp
        left += 1
        right -= 1

    return str


ls = ['h', 'e', 'l', 'l', 'o']
print(reverse_string(ls))
