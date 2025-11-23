# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
       
        s=set()
        
        while slow:
            if slow.next==None:
                return None
            
            if slow in s:
                return slow
            s.add(slow)
            print(slow.val)
            slow=slow.next
        return None
           