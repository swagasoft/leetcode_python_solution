

# Example 1:

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# Example 2:

# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.
# Example 3:

# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        lenn = len(heights)
        list2 = [item for item in heights]
        list2.sort()

        for i in range(lenn):
            if heights[i] != list2[i]:
                result += 1

        return result
