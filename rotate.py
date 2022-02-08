

class Solution:
    def rotate(nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        last = len(nums) - 1

        while start < k:
            last_ele = nums[last]
            nums.pop()
            nums.insert(0, last_ele)
            start += 1

        return nums

    my_list = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(my_list, k))
