def call_point(ls: list):
    result = []
    if len(ls) == 1:
        return ls
    for i in range(len(ls)):
        ele = ls[i]
        if ele == '+':
            result.append(result[-1] + result[-2])
        elif ele == 'C':
            result.pop()
        elif ele == 'D':
            result.append(2 * result[-1])
        else:
            result.append(int(ele))

    return sum(result)


# arr = ['5', '2', 'C', 'D', '+']
arr = ['5', '-2', '4', 'C', 'D', '9', '+', '+   ']
print(call_point(arr))
