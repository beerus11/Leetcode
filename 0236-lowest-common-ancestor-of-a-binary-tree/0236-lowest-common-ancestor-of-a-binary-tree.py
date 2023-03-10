# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root ==p:
            return p
        if root==q:
            return q
        if not root.left:
            return self.lowestCommonAncestor(root.right,p,q)
        if not root.right:
            return self.lowestCommonAncestor(root.left,p,q)
            
        a = self.lowestCommonAncestor(root.left,p,q)
        b = self.lowestCommonAncestor(root.right,p,q)
        
        if a and b:
            return root
        if not a:
            return b
        return a