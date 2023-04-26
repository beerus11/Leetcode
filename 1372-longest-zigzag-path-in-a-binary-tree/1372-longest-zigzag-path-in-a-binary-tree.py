# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def lp(node,c,d):
            if not node:
                return
            self.res = max(self.res,c)
            if d:
                lp(node.left,c+1,False)
                lp(node.right,1,True)
            else:
                lp(node.left,1,False)
                lp(node.right,c+1,True)
        lp(root,0,False)
        lp(root,0,True)
        return self.res
        
        