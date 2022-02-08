class Solution:
    @classmethod
    def minSubArrayLen(self, target: int, nums: list) -> int:
        
        i = 0
        j = 0
        sub_sum = 0
        sub_len = float('inf')
        
        while i < len(nums):
            if sub_sum < target:
                sub_sum += nums[i]
                i+= 1
            while sub_sum >= target:
                if i - j < sub_len:
                    sub_len = i -j
                sub_sum -= nums[j]
                j+= 1
                
        if sub_len == float('inf'):
            return 0
        else:
            return sub_len

# print(Solution.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
# print(Solution.minSubArrayLen(7,[2,3,1,2,4,3]))
print(Solution.minSubArrayLen(7,[3,1,4,3,2,1,4]))
        
        

            
        