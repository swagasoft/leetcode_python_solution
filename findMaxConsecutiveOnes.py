class Solution:
    def findMaxConsecutiveOnes( nums) -> int:
        maxNumCount = 0
        result = 0

        for num in nums:
            print(num)
            if num == 1:
                maxNumCount += 1
                if maxNumCount > result:
                    result = maxNumCount
            else:
                maxNumCount = 0

        return result
