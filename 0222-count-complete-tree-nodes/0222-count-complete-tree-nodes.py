# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def l(node):
            h = 0
            while node:
                h+=1
                node = node.left
            return h
        def r(node):
            h = 0
            while node:
                h+=1
                node = node.right
            return h
        def fn(root):
            if not root:
                return 0
            lh = l(root.left)
            rh = r(root.right)
            if lh==rh:
                return (2**(lh+1)) -1
            return 1+ fn(root.left)+fn(root.right)
        return fn(root)
    