
def parity(x:int):
    result = 0
    while x:
        result ^=  x + 1
        x >>= 1
        return x

print(parity(30))