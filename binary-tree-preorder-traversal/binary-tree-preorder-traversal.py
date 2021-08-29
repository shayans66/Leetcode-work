# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        
        self.helper(root.left, arr)
        self.helper(root.right, arr)
        
        
    