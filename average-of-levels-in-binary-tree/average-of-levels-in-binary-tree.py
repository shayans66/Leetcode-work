# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    
        que = [root]
        res = []
        currow = []
        while que:
            l = len(que)
            for i in range(l):
                node = que.pop(0)

                currow.append(node.val)
                
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                    
            avg = sum(currow)/len(currow)
            res.append(avg)
            currow = []
        return res  
