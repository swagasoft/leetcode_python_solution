

from typing import List


class Solution:
    @classmethod
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0
        
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        
        return max_sub
ls = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(ls))