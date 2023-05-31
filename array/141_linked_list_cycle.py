# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def __init__(self):
      self.head = None
      
      
    def insert_at_head(self, data):
        new_node = ListNode(data)
        if(self.head is None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
      
      
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            print("fast ", fast)
            print("fast_next ", fast.next)
            slow = slow.next
            fast =  fast.next.next
            
            if fast == slow:
                return True
            
        return False
    
    
solution = Solution()
solution.insert_at_head(4)
solution.insert_at_head(6)
solution.insert_at_head(9)
solution.insert_at_head(45)
print('result ', solution.hasCycle(solution.head))
        
    
            
            
        
            
            
        