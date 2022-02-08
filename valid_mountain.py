# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true


class Solution(object):
    def validMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        inc = False
        dec = False

        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                if inc == False:
                    return False
                else:
                    dec = True

            elif (arr[i + 1] > arr[i]):
                if (dec == True):
                    return False
                inc = True
            else:
                return False

        if inc and dec:
            return True
        else:
            return False
    val = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(validMountainArray(val))
