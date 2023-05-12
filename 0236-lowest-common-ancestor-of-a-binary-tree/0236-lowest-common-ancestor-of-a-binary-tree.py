# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            a = lca(node.left)
            b = lca(node.right)
            if a and b:
                return node
            return a if not b else b
        return lca(root)
        