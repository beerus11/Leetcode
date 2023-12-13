# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.result = -1e9
        def get_avg(node):
            if not node:
                return 0, 0 
            
            nl, sl = get_avg(node.left)
            nr, sr = get_avg(node.right)
            n = nl + nr+ 1
            s = node.val + sl + sr
            self.result = max(self.result, s/n)
            return n, s
        get_avg(root)
        return self.result
        