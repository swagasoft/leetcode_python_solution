# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution(object):
    def moveZeroes(nums: list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums) - 1
        i = 0

        while length >= i:
            if(nums[length] == 0):
                del nums[length]
                nums.append(0)
                length -= 1
            else:
                length -= 1

        print('final', nums)
        # for item in reversed(nums):
        #     print(item)
        #     if item == 0:
        #         del item

        return nums

    ls = [0, 0, 1]
    # ls = [1, 0, 3, 12, 0]
    print(moveZeroes(ls))
