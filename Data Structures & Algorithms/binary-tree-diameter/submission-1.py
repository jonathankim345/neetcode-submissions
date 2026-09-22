# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def find_height(root):
            nonlocal diameter
            if not root: 
                return 0 
            left = find_height(root.left)
            right = find_height(root.right)
            d = left + right
            diameter = max(d, diameter)
            return 1 + max(left, right)
        find_height(root)
        return diameter