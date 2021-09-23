# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while True:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # one is equal to cur, or is greater one is less
            else:
                return cur
            # elif p.val == cur.val and q.val == cur.val:
            #     return cur
        return cur
            
        
        
        
#         if not p or not q:
#             return None
        
#         # ans = self.isSubChild(root, p) and self.isSubChild(root, q)
        
#         ans = None
#         l,r = root.left, root.right

#         ans = root if (self.isSubChild(root,p) and self.isSubChild(root,q)) else None
        
        
        
# #         while l:
# #             ans = l if (self.isSubChild(l,p) and self.isSubChild(l,q)) else ans
# #             l = l.left
# #         while r:
# #             ans = r if (self.isSubChild(r,p) and self.isSubChild(r,q)) else ans
# #             r = r.right
            
            
            
#         return ans
        
#     def isSubChild(self, r, c):
#         if not r or not c:
#             return False
#         if r == c:
#             return True
#         return self.isSubChild(r.left, c) or self.isSubChild(r.right, c)