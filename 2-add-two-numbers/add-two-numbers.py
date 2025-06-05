# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        res=head
        t=c=0

        while l1 or l2 or c:
            t=c
            if l1:
                t+=l1.val
                l1=l1.next
            if l2:
                t+=l2.val
                l2=l2.next
            num=t%10
            c=t//10
            head.next=ListNode(num)
            head=head.next
        return res.next
        