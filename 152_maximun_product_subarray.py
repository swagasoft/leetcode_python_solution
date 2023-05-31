from typing import List


class Solution:
    @classmethod
    def maxProduct(self, nums: List[int]) -> int:
        nums2 = nums[::-1]
        
        for i in range(1, len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
            if nums2[i-1] != 0:
                nums2[i] *= nums2[i-1]
                
        return max(nums + nums2)
# ls = [2,-5,-2,-4,3]
ls = [2,3,-2,4]
print(Solution.maxProduct(ls))


        
