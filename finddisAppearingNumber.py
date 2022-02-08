class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        l = len(nums)
        nums = set(nums)

        for i in range(1, l + 1):
            print('index ', i)

            if i not in nums:
                result.append(i)

        return result
