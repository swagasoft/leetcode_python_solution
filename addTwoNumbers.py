# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    @classmethod
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]):
        dummyNode = ListNode(0)
        carry = 0
        current = dummyNode
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1 = 0
                
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
                
            currentSum = l1_val + l2_val + carry
            current.next = ListNode(currentSum % 10)
            current =  current.next
            carry = currentSum // 10
            
            if l1:
                l1 =  l1.next
            if l2:
                l2 = l2.next
                
            if carry:
                current.next = ListNode(carry)
            
        return  dummyNode.next
        

l1 = [2,4,3]
l2 = [5,6,4]

print(Solution.addTwoNumbers(l1, l2))