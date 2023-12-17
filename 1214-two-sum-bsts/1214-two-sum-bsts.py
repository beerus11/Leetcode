# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node,s):
            if not node:
                return
            s.add(node.val)
            dfs(node.left,s)
            dfs(node.right,s)
        s1 = set()
        dfs(root1,s1)
        def check(node):
            if not node:
                return
            if target-node.val in s1:
                return True
            return check(node.left) or check(node.right)
        return check(root2)