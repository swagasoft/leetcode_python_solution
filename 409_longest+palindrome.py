from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        output = 0
        
        for count in c.values():
            output += int(count/2) * 2
            if output % 2 == 0  and  count % 2 == 1:
                output += 1
                
        return output



    #     class Solution:
    # def longestPalindrome(self, s):
    #     ans = 0
    #     for v in collections.Counter(s).itervalues():
    #         ans += v / 2 * 2
    #         if ans % 2 == 0 and v % 2 == 1:
    #             ans += 1
    #     return ans
        