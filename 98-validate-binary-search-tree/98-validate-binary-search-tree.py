# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isOk(root: Optional[TreeNode], mn=-math.inf, mx=math.inf):
            if not root:
                return True
#            print(root)
            if root.val <= mn or root.val >= mx:
                return False
            return isOk(root.left, mn, root.val) and isOk(root.right, root.val, mx)
            
        return isOk(root)