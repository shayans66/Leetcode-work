# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res, stack = [], []
            p = root
            
            while stack or p:
                if p:
                    stack.append(p)
                    p = p.left
                else:
                    node = stack.pop()
                    res.append(node.val)
                    p = node.right
            return res
            
            
            
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