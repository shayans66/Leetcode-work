# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        if root.val == subRoot.val and self.equalTrees(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        
    def equalTrees(self,a,b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            if a.val != b.val:
                return False
            return self.equalTrees(a.left,b.left) and self.equalTrees(a.right,b.right)
        