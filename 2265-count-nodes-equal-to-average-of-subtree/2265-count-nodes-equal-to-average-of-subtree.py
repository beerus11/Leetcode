# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return 0,0
            a,c1 = dfs(node.left)
            b,c2 = dfs(node.right)
            if (a+b+node.val)//(1+c1+c2) == node.val:
                self.count+=1
            return a+b+node.val,1+c1+c2
        dfs(root)
        return self.count