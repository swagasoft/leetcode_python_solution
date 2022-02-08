class Solution:
    def longestOnes( nums: list, k: int) -> int:

        left, maximum = 0, 0

        for i,val in enumerate(nums):
            k -= (1- val)
            if k < 0:
                k += (1- nums[left])
                left += 1
            maximum = max(maximum, i-left+ 1)

        return maximum

                
            
   
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution.longestOnes(nums, k,))


                        