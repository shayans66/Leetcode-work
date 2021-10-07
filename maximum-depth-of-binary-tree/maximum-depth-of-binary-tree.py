# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         maxlen = curlen = 1 if root else 0
#         stack = []
        
#         cur = root
        
#         while cur or stack:
#             if cur.left:
#                 if cur.right:
#                     stack.append([cur.right, curlen+1])
#                 cur = cur.left
#                 curlen += 1
#                 maxlen = max(maxlen, curlen)
#             elif cur.right:
#                 cur = cur.right
#                 curlen += 1
#                 maxlen = max(maxlen, curlen)
#             else:
#                 maxlen = max(maxlen, curlen)
#                 if stack: 
#                     tup = stack.pop()
#                     cur = tup[0]
#                     curlen = tup[1]
#                 else: cur = None
            
#         return maxlen
                    
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))