# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=[]
        y=head
        while head:
            x.append(head.val)
            head=head.next
        del x[-n]
        print(x)
        q=y
        l=len(x)
        if l==0:
            return None
        for i,j in enumerate(x):
            l-=1
            print(i,j)
            y.val=j
            if l==0:
                y.next=None
                break
            y=y.next
            
        
        return q
        