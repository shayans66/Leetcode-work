# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or self.hasAll0(root):return
        
        if self.hasAll0( root.left):
            root.left = None
        if self.hasAll0(root.right):
            root.right = None
            
        self.pruneTree(root.left)
        self.pruneTree(root.right)
        
        return root
    
    def hasAll0(self, root: Optional[TreeNode]):
        if not root: return True
        if root.val != 0:
            return False
        return self.hasAll0(root.left) and self.hasAll0(root.right)
        
        
#         if root and root.left and root.left.val == 0 and not root.left.left and not root.left.right:
#             root.left = None
#         if root and root.right and root.right.val == 0 and not root.right.left and not root.right.right:
#             root.left = None
        
#         if root.left: self.pruneTree(root.left)
#         if root.right: self.pruneTree(root.right)
#         return root
        