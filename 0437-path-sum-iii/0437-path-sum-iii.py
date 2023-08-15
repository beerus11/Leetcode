# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.h = defaultdict(int)
        self.count = 0
        def dfs(node,curr_sum):
            if not node:
                return
            curr_sum+=node.val
            if curr_sum == targetSum:
                self.count+=1
            
            self.count += self.h[curr_sum-targetSum]
            self.h[curr_sum]+=1
            
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            
            self.h[curr_sum]-=1
            
        dfs(root,0)
        return self.count