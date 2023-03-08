# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def s(node,l,h):
            if not node:
                return 0
            if node.val>high:
                return s(node.left,l,node.val)
            if node.val<low:
                return s(node.right,node.val,h)
            return node.val+s(node.left,l,node.val)+s(node.right,node.val,h)
        return s(root,low,high)
        