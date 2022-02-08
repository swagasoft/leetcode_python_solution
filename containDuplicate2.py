from lib2to3.pgen2.token import GREATER


class Solution:

    # Slidding window

    @classmethod
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:

        myMap = dict()

        for i, num in enumerate(nums):
            if num in myMap:
                if abs(i - myMap[num]) <= k:
                    return True
                else:
                    del myMap[num]
                    myMap[num] = i
            else:
                myMap[num] = i

        return False


# nums = [1, 2, 3, 1, 2, 3]
# k = 7
# nums = [1, 2, 3, 1]  # True
# k = 3

# nums = [1, 0, 1, 1]  # True
# k = 1
nums = [1, 2, 3, 1, 2, 3]  # False
k = 2
# nums = [1, 0, 1, 1]
# k = 1

print(Solution.containsNearbyDuplicate(nums, k))
