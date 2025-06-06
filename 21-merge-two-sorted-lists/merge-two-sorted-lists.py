# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode()
        res=dum
        while l1 or l2:
            if l1 != None and l2!=None:
                if l1.val<l2.val:
                    dum.next=ListNode(l1.val)
                    l1=l1.next
                else:
                    dum.next=ListNode(l2.val)
                    l2=l2.next
            else:
                if l1:
                    dum.next=ListNode(l1.val)
                    l1=l1.next
                if l2:
                    dum.next=ListNode(l2.val)
                    l2=l2.next
            dum=dum.next
            
       
        return res.next

        