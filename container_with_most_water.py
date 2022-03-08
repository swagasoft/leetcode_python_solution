class Solution:
    @classmethod
    def maxArea(self, height:list) -> int:
        
        left = 0
        right = len(height) - 1
        maxWater = 0
        
        while left <  right:
            maxWater = max(maxWater , min(height[left] , height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxWater
        

height = [1,3,6,2,5,4,1,3,7]
print(Solution.maxArea(height))

        