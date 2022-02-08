
def longest_pallindrome_substring(string: str):
    lenn = len(string)
    if len(string) < 1:
        return ''

    start = 0
    end = 0

    for i in range(lenn):
        len1 = expandArroundCenter(s, i, i)
        len2 = expandArroundCenter(s, i, i+1)

        len_max = max(len1, len2)


def expandArroundCenter(s, left, right):
    left2 = left
    right2 = right

    while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
        left2 -= 1
        right2 += 1
    return right - left2 - 1
