# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count =0
        self.no = -1
        def dfs(node):
            if not node:
                return
            if self.count==k:
                return
            dfs(node.left)
            if self.count<k:
                self.count +=1
                self.no = node.val
            if self.count<k:
                dfs(node.right)
        dfs(root)
        return self.no
        