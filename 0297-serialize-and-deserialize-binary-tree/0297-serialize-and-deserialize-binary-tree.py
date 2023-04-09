# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.data = []
        def s(node):
            if not node:
                self.data.append("None")
                return 
            self.data.append(str(node.val))
            s(node.left)
            s(node.right)
        s(root)
        print(self.data)
        return ",".join(self.data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque(data.split(","))
        def ds():
            n = q.popleft()
            if n=="None":
                return None
            node = TreeNode(n)
            node.left = ds()
            node.right = ds()
            return node
        return ds()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))