# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = {}
        self.ans = -1
        def dfs(node,l,p):
            if node==None:
                return
            if l not in m:
                m[l]=p
            self.ans = max(self.ans,p-m[l]+1)
            dfs(node.left,l+1,p*2)
            dfs(node.right,l+1,2*p+1)
        dfs(root,0,0)
        #print(mx,mn)
        return self.ans
        