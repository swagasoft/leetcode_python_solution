from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if (leftSum == rightSum):
                return i
            leftSum += nums[i]
            
        return -1
        
classInstance = Solution()
# nums = [1,2,3]
# nums = [1,7,3,6,5,6]
nums = [2,1,-1]
print(classInstance.pivotIndex(nums))