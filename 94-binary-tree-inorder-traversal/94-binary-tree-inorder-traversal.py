# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res, stk = [], []
            cur = root
            
            while cur or stk:
                while cur:
                    stk.append(cur)
                    cur = cur.left
                cur = stk.pop()
                res.append(cur.val)
                cur = cur.right
            return res
            
#            res, stack = [], []
#            p = root
#            
#            while stack or p:
#                if p:
#                    stack.append(p)
#                    p = p.left
#                else:
#                    node = stack.pop()
#                    res.append(node.val)
#                    p = node.right
#            return res

#            ans = []
#            self.helper(root, ans)
#            return ans
#
#        def helper(self, root, arr):
#            if not root:
#                return
#            self.helper(root.left, arr)
#            arr.append(root.val)
#            self.helper(root.right, arr)
            
            
            
#             public List<Integer> inorderTraversal(TreeNode root) {
#     List<Integer> result = new ArrayList<>();
#     Deque<TreeNode> stack = new ArrayDeque<>();
#     TreeNode p = root;
#     while(!stack.isEmpty() || p != null) {
#         if(p != null) {
#             stack.push(p);
#             p = p.left;
#         } else {
#             TreeNode node = stack.pop();
#             result.add(node.val);  // Add after all left children
#             p = node.right;   
#         }
#     }
#     return result;
# }