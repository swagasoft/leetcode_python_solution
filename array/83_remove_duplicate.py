
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Remove duplicate from sorted list
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr  and curr.next:
            if  curr.val ==  curr.next.val:
                curr.next =  curr.next.next
            else:
                curr = curr.next
                
        return head
        