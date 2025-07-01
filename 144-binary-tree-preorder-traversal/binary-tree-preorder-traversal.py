# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rr=[]
        def travel(r):
            if r==None:
                return
            rr.append(r.val)
            travel(r.left)
            travel(r.right)
        travel(root)
        return rr
        