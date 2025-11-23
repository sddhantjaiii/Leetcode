# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            temp=temp.next
            c+=1
        x=c-n
        count=0
        ptr=head
        while ptr:
            count+=1
            print(count,x)
            if x==0:
                if head.next:
                    return head.next
                return None
            if count==x:
                
                ptr.next=ptr.next.next
            ptr=ptr.next
        return head
        