# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        root = self.putMidInBST(nums, 0, len(nums)-1)
        return root

    def putMidInBST(self, nums, l, r):
        if l > r:
            return None
        m = l + (r-l)//2
        val = nums[m]
        
        # if not root:
        #     root = TreeNode(val)
        # else:
        #     if val < root.val:
        #         root.left = TreeNode(val)
        #     elif val > root.val:
        #         root.right = TreeNode(val)
        
        root = TreeNode(val)
        
        root.left = self.putMidInBST(nums, l, m-1)
        root.right = self.putMidInBST(nums, m+1, r)
        
        return root
        
        
#         if not nums:
#             return None
        
#         l, r = 0, len(nums)-1
#         mid = l + (r-l)/2
#         root = TreeNode(nums[mid])
        
        
#         while l <= r:
#             mid = l + (r-l)/2
            
            
        
#     def insert(root, val):
#         cur = root
#         while cur:
#             if cur.val < val:
#                 if cur.left:
#                     cur = cur.left
#                 else:
#                     cur.left = TreeNode(val)
#                     return
#             elif cur.val > val
#                 if cur.right:
#                     cur = cur.right
#                 else:
#                     cur.right = TreeNode(val)
#                     return
#             else:
#                 return