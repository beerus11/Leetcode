# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        d = defaultdict(int)
        def dfs(node):
            if not node:
                return ""
            rep = ("(" + dfs(node.left)+ ")" +str(node.val)+ "(" +dfs(node.right)+ ")")
            d[rep]+=1
            if d[rep]==2:
                ans.append(node)
            return rep
                
        dfs(root)
        return ans
                
        