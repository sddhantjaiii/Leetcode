# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h=[]
        c=0
        res=ListNode()
        k=res
        while any(x for x in lists):
            mm=[float('inf'),0]
            for j in range(len(lists)):
                i=lists[j]
                if i==None:
                    continue
                m=i.val
                if m<=mm[0]:
                    mm[0]=m
                    mm[1]=j
            res.next=ListNode(lists[mm[1]].val)
            res=res.next
            lists[mm[1]]=lists[mm[1]].next
            
            c+=1
        return k.next


            