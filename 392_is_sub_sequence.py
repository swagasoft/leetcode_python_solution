class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        point1 = point2 = 0
        
        while point1 < len(s) and point2 < len(t):
            if s[point1] == t[point2]:
                point1 += 1
            point2 += 1
            
        return point1 == len(s)

                
        
                
s = "abc"
t = "ahbgdc"

classInstance = Solution()
print(classInstance.isSubsequence(s,t))