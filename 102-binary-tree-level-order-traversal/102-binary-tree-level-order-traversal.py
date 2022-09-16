# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # https://www.techiedelight.com/level-order-traversal-binary-tree/
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        def helper(node, level):
            if len(ans) == level:
                ans.append([])
            
            ans[level].append(node.val)
            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
#            if level == 1:
#                ans[level].append(root.val)
#                return
#            l = helper(root.left, level-1)
#            r = helper(root.right, level-1)
#            
#            return left or right
        
        lvl = 0
        while helper(root, lvl):
            lvl+=1
        return ans
            
            
                
        
        
#    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#        if not root:
#            return []
#        q = [root]
#        ans =[]
#        
#        while q:
#            n = q.pop(0)
#            ans.append(n.val)
#            if n.left:
#                q.append(n.left)
#            if n.right:
#                q.append(n.right)
#        return [ans]