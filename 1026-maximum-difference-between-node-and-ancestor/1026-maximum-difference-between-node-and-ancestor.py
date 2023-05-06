# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        def dfs(node,mx,mn):
            if not node:
                return
            self.ans = max(self.ans,max(abs(mx-node.val),abs(mn-node.val)))
            
            new_mx = max(mx,node.val)
            new_mn = min(mn,node.val)
            dfs(node.left,new_mx,new_mn)
            dfs(node.right,new_mx,new_mn)
            
        dfs(root,root.val,root.val)
        return self.ans
            
        