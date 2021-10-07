# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = self.minDepth

        def height(root):
            if not root:
                return 0
            return 1 + height(root)
        
        if not root:
            return 0
        # return 1+min(minDepth(root., minDepth(root.right))
        psb = []
        if root.left: psb.append(root.left)
        if root.right: psb.append(root.right)
            
        arr = [minDepth(el) for el in psb]

        return 1+min(arr) if arr else 1