# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head.next
        while fast:
            if not fast.next:
                slow.next=slow.next.next
                return head
            if fast.next.next==None:
                
                slow.next=slow.next.next
                return head
            slow=slow.next
            fast=fast.next.next
        