# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t=set()
        x=head
        while x not in t:
            if x==None:
                return False
            if x.next==None:
                return False
            t.add(x)
            x=x.next
        return True