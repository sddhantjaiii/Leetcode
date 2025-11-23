# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        if not head:
            return head
        even=head.next
        saveo=odd
        savee=even
        while odd.next and even.next:

            odd.next=even.next
            even.next=odd.next.next
            even=even.next
            odd=odd.next
        odd.next=savee
        return head
        