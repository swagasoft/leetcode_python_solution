


from typing import List


class Solution:

    @classmethod
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        string_value = ''
        # convert list of number to string
        for i in digits:
            string_value += str(i)
            
         # convert to number to integer
        num_value = int(string_value)
        strss = str(num_value + 1)
        #  convert to to list
        for i in strss:
            result.append(int(i))
        return result


print(Solution.plusOne([9,9]))
        

        


    

