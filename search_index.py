class Solution:
    def search(nums: list, target: int) -> int:

        if len(nums) == 0:
            return nums

        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

#             left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

#             right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))
