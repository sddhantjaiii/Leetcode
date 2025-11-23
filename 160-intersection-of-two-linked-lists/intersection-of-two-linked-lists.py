# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        t1=headA
        t2=headB
        c=0
        while headA and headB:
            if headA==headB:
                return headA
            if (not headA.next) and (not headB.next):
                return None
            if headB.next==None:
                headB=t1
                headA=headA.next
                continue
            if headA.next==None:
                headA=t2
                headB=headB.next
                continue
            
            
            
            headA=headA.next
            headB=headB.next
        return None
        