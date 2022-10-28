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
            
            diff = abs(target-node.val)
            
            if target<node.val:
                dfs(node.left)
            else:
                dfs(node.right)
                
            if diff<self.mn:
                self.mn = diff
                self.node = node.val
                
        dfs(root)
        return self.node
            