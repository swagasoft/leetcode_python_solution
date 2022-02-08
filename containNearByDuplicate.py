# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


class Solution:
    @classmethod
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        
        window =  dict()

        for  count,val in  enumerate(nums):
            if  val in window.values():
                return True
            window[count] = val

            if len(window) - 1 >= k:
                del window[count - k]

        return False


        
     
            
nums =[0,1,2,3,2,5]
k = 3
# print(Solution.containsNearbyDuplicate(nums,k))  
print(Solution.containsNearbyDuplicate([1,2,3,1],3))  
# print(Solution.containsNearbyDuplicate([1,2,3,1,2,],2))  
       