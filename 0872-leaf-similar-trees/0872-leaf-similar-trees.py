# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def ls(node,sq):
            if not node:
                return
            if not node.left and not node.right:
                sq.append(node.val)
            ls(node.left,sq)
            ls(node.right,sq)
            return sq
        
        return ls(root1,[])==ls(root2,[])