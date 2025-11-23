# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        s1=set()
        while headA or headB:
            if headA:
                s.add(headA)
            if headB:
                s1.add(headB)
            if headA in s1 :
                return headA
            if headB in s:
                return headB
            if headA:
                headA=headA.next
            if headB:
                headB=headB.next
        return None
        