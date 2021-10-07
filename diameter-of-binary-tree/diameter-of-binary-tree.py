# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diam = 0
        a=[]
        
        def findDiam(root):
            a.append(1)
            if not root:
                return 0
            nonlocal diam
            
            leftH = findDiam(root.left)
            rightH = findDiam(root.right)
            
            diam = max(diam, leftH + rightH)
            
            return 1+max(leftH, rightH)
        
        findDiam(root)
        
        
        return diam