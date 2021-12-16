# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(n):
            if not n:
                res.append('N')
                return
            res.append(str(n.val))
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        arr = data.split(',')
        self.i = 0
        def dfs():
            if arr[self.i] == 'N':
                self.i+=1
                return None
            n = TreeNode(int(arr[self.i]))
            self.i+=1
            n.left=dfs()
            n.right= dfs()
            return n
        return dfs()
            
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans