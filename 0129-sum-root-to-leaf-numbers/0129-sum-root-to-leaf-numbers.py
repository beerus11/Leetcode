# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ts = 0
        def dfs(node,t):
            if not node:
                return 0
            if not node.left and not node.right:
                return t*10+node.val
            x = t*10 + node.val
            return dfs(node.left,x)+dfs(node.right,x)
        return dfs(root,0)