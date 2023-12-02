# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def ps(node,arr,s):
            if not node:
                return
            arr.append(node.val)
            ps(node.left,arr,s+arr[-1])
            ps(node.right,arr,s+arr[-1])
            if not node.left and not node.right and s+arr[-1]==targetSum:
                self.ans.append(arr[:])
            arr.pop()
        ps(root,[],0)
        return self.ans
            
        