# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = 0
        
        def inorderTraversal(root):
            nonlocal prev
            if not root:
                return
            inorderTraversal(root.right)
            root.val += prev
            prev = root.val
            inorderTraversal(root.left)
            return
        
        inorderTraversal(root)
        return root