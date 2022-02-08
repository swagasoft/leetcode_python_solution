# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x <= 1):
            return x
        else:
            return int(floor(sqrt(x)))
