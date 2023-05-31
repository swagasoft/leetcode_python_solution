from typing import List


class Solution:
    @classmethod
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right =mid - 1
            else:
                left = mid + 1
                
        return left

ls , target = [1,3,5,6], 5

print(Solution.searchInsert(ls, target))
            
            
            
            
        