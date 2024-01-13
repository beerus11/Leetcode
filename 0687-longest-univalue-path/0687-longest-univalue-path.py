# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def dfs(node,prev_value):
            if node==None:
                return 0
            
            l = dfs(node.left,node.val)
            r = dfs(node.right,node.val)
            
            self.ans = max(self.ans,l+r)
            return max(l,r)+1 if node.val == prev_value else 0
        
                
        dfs(root,-1)
        return self.ans
        