
from typing import List


class Solution:
    @classmethod
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]*len(nums)  # [1,1,1,1]
        prefix = 1
        postfix = 1
        
        for i in range(0,len(nums)):
            
            ans[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            
            ans[i] = ans[i] * postfix
            postfix *= nums[i]
           
        return ans

print(Solution.productExceptSelf([1,2,3,4]))