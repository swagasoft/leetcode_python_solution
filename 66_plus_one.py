


from typing import List


class Solution:

    @classmethod
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        stringNum = ''
        # convert list of number to number string
        for i in digits:
            stringNum += str(i)
            
        # convert number string to integer
        ans = int(stringNum)
        # add the one to the number and convert to string number
        strss = str(ans + 1)
        # 
        for i in strss:
            result.append(int(i))
        return result

        
ls = [1,2,3]
print(Solution.plusOne(ls))


    

