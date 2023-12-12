# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.hm = defaultdict(list)
        def dfs(node,h):
            if node is None:
                return
            self.hm[h].append(node.val)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        dfs(root,0)
        return self.hm[len(self.hm)-1][0]
        