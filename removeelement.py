# pylint: disable=unsubscriptable-object
class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        length = len(nums) - 1

        while i <= length:
            if nums[i] == val:
                del nums[i]
                length -= 1
            else:
                i += 1

        print('final ', nums)

    removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
