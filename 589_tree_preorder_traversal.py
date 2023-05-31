"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        output = []
        
        def dfs(node):
            if not node: 
                return
            else:
                output.append(node.val)
                
            for child in node.children:
                dfs(child)
                
        dfs(root)
        
        return output
        
root = [1,null,3,2,4,null,5,6]
#  root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        