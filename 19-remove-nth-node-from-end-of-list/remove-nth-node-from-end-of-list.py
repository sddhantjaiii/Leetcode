class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        curr=head
        l=0
        while cur:
            cur=cur.next
            l+=1
            
        c=1
        
        if l==n:
            return head.next
        while c<l-n:
            curr=curr.next
            c+=1
        curr.next=curr.next.next
        
        return head        