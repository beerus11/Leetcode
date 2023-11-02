# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0,0
            sl,cl = dfs(node.left)
            sr,cr = dfs(node.right)
            avg = (sl+sr+node.val)//(cl+cr+1)
            if node.val == avg :
                self.ans +=1
            return sl+sr+node.val,cl+cr+1
        dfs(root)
        return self.ans
        