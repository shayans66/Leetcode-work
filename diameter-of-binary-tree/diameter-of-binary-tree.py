# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a = self.height(root.right) + self.height(root.left)
        
        b = self.diameterOfBinaryTree(root.left)
        c = self.diameterOfBinaryTree(root.right)
        
        return max(a,b,c)
        
    def height(self, root):
        if not root:
            return 0
        left = 1 + self.height(root.left)
        right = 1 + self.height(root.right)
        
        return max(left, right)