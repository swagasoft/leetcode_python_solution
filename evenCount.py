# pylint: disable=not-an-iterable
import math


class Solution:
    def findNumbers(nums) -> int:
        evenCount = 0
        for num in nums:
            digit = int(math.log10(num)) + 1
            print('see ', digit)
            if digit > 0:
                if digit % 2 == 0:
                    evenCount += 1

        return evenCount

    print(findNumbers([10, 2000, 3, 50, 240]))
