# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None: return []
        result, queue = [],[]
        queue.append(root)
        while queue:
            count = len(queue)
            level_node = []
            for i in range(count):
                node = queue[0]
                queue.pop(0)
                if node.left != None: queue.append(node.left)
                if node.right != None: queue.append(node.right)
                level_node.append(node.val)
            
            result.append(level_node)
            
        return result


inputData = [3,9,20,None,None,15,7]
solutionInstance = Solution()
print('result ', solutionInstance.levelOrder(inputData))