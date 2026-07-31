# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next==None:
            return None
        temp=head
        count=0
        while temp!=None:
            temp=temp.next
            count+=1
        p=head
        if count == n:
            head=head.next
            return head
        for i in range(count-n-1):
            p=p.next
        p.next=p.next.next
        return head
            
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        