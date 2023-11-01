# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = defaultdict(int)
        self.mxc = 0
        def dfs(node):
            if not node:
                return
            hm[node.val]+=1
            self.mxc = max(self.mxc,hm[node.val])
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return [k for k,v in hm.items() if v==self.mxc]
        