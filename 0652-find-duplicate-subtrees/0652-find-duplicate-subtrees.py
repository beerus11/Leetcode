# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.hm = defaultdict(int)
        self.res = []
        def dfs(node):
            if not node:
                return ''
            l,r = dfs(node.left),dfs(node.right)
            struct = 'l%s_%s_%sr'%(l,str(node.val),r)
            self.hm[struct]+=1
            if self.hm[struct]==2:
                self.res.append(node)
            return struct
        dfs(root)
        return self.res
                