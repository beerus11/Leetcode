# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ib(node):
            if not node:
                return True, -1
            lb,lh = ib(node.left)
            if not lb:
                return False,0
            rb,rh = ib(node.right)
            if not rb:
                return False,0
            return abs(lh-rh)<2,1+max(lh,rh)
        return ib(root)[0]
        