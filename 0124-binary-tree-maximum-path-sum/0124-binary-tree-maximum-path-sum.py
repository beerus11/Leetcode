# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mxp = float('-inf')
        def mps(node):
            if not node:
                return 0
            left = max(mps(node.left),0)
            right = max(mps(node.right),0)
            self.mxp = max([self.mxp,node.val+left+right])
            return node.val+max(left,right)
        mps(root)
        return self.mxp
        