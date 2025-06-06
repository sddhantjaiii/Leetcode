# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        curr=head
        l=0
        while cur:
            cur=cur.next
            l+=1
            
        c=1
        if l==1:
            return head.next
        if l==n:
            return head.next
        while c<l-n:
            curr=curr.next
            c+=1
        curr.next=curr.next.next
        cur=head
        
        return head        