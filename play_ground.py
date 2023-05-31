
import collections
from typing import List


def play_method(numbers :List, target: int):

    occur = 0

    for index in range(len(numbers)):

        current_val = numbers[index]
        if target == current_val: occur += 1

    return occur
    

lenn = [3,5,6,3,4,8,9,4,5,3,4,4,4,2,1,4]
print(play_method(lenn, 4))
print(pow(10,3,1))