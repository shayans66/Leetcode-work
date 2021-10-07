# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left), height(root.right))
        
        def diamOfNode(root):
            return height(root.left) + height(root.right)
            
        # diameterOfBinaryTree= self.diameterOfBinaryTree
        
        stk = []
        res = 0
        if root: stk.append(root)
        while stk:
            node = stk.pop()
            # print(f'res: {res}')
            res = max(res, diamOfNode(node))
            
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        return res