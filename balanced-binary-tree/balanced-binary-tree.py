# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        nodeIsBalanced = self.nodeIsBalanced
        isBalanced = self.isBalanced
        return nodeIsBalanced(root) and isBalanced(root.left) and isBalanced(root.right)
        
        
    def nodeIsBalanced(self, root):
        l = (root and root.left) or None
        r = (root and root.right) or None
        return abs(self.height(l) - self.height(r)) <= 1
        
    def height(self, root):
        if not root:
            return 0
        height = self.height
        return 1 + max(height(root.left), height(root.right))