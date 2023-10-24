# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        m = {}
        def dfs(node,l):
            if not node:
                return
            if l not in m:
                m[l]=node.val
            else:
                m[l]=max(m[l],node.val)
            dfs(node.left,l+1)
            dfs(node.right,l+1)
        dfs(root,0)
        ans = []
        for i in range(len(m)):
            ans.append(m[i])   
        return ans  
            
        