# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]

        def inorder(root,l):
            if root is not None:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
        inorder(root,l)
        return l
            

