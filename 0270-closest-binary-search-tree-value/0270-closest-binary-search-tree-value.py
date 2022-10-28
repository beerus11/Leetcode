# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.mn = float('inf')
        self.node = None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            diff = abs(target-node.val)
            if diff<self.mn:
                self.mn = diff
                self.node = node.val
            dfs(node.right)
        dfs(root)
        return self.node
            