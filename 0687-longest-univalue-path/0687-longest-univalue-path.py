# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        self.ans = 1
        def lp(node):
            if node==None:
                return 0,-10001
            left_cnt,left_value = lp(node.left)
            right_cnt,right_value = lp(node.right)
            if left_value!=node.val and right_value!=node.val:
                return 1,node.val
            if left_value==node.val and right_value==node.val:
                l = left_cnt+1
                r = right_cnt+1
                self.ans = max(self.ans,left_cnt+right_cnt+1)
                return max(l,r),node.val
            if left_value==node.val:
                l = left_cnt+1
                self.ans = max(self.ans,l)
                return l,node.val
            r = right_cnt+1
            self.ans = max(self.ans,r)
            return r,node.val
        lp(root)
        return self.ans-1
            
        