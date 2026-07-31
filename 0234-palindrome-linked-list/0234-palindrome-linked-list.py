# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow!=None:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        


        
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        