# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2 or r1.val != r2.val:
                return False

            return equal(r1.left, r2.left) and equal(r1.right, r2.right)
        
        if not subRoot: return True
        if not root: return False
        if equal(root, subRoot):
            return True
        l, r = root.left if root else None, root.right if root else None
        return self.isSubtree(l, subRoot) or self.isSubtree(r, subRoot)
        
        
