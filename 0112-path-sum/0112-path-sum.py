# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,t):
            if not node:
                return False
            if node.val ==t and not node.left and not node.right:
                return True
            return dfs(node.left,t-node.val) or dfs(node.right,t-node.val)
        return dfs(root,targetSum)
        