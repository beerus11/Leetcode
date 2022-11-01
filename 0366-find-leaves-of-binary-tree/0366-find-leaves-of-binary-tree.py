# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.hm = defaultdict(list)
        def height(node):
            if not node:
                return 0
          
            l = height(node.left)
            r = height(node.right)
            
            h = 1+max(l,r)
            self.hm[h].append(node.val)
            return h
        height(root)
        return self.hm.values()