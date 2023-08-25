# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                return node
            tail_left = dfs(node.left)
            tail_right = dfs(node.right)
            
            if tail_left:
                tail_left.right = node.right
                node.right = node.left
                node.left = None

            return tail_right if tail_right else tail_left
        return dfs(root)
            
        