


from typing import List


class Solution:
    def runningSum( nums: List[int]) -> List[int]:
        
        result = []
        for index, val in enumerate(nums):
            tempIndex = index
            currValue = nums[index]
            # tempIndex =  tempIndex - 1
            while tempIndex > 0:
                tempIndex = tempIndex - 1
                currValue += nums[tempIndex]
               
                
            result.append(currValue)
            
        return result

    test_case = [1,1,1,1,1]           
    test_case = [1,2,3,4]           
    print(runningSum(test_case))