# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, lower, upper):
            if root is None:
                return True
            if not(lower < root.val < upper):
                return False
            if not traverse(root.left, lower, root.val):
                return False
            if not traverse(root.right, root.val, upper):
                return False
            return True
        return traverse(root, -10**5, 10**5)
        
            