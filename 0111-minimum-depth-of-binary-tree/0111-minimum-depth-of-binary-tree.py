# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode],depth=0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        min_depth = float('inf')
        for c in [root.left,root.right]:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return 1+min_depth
        