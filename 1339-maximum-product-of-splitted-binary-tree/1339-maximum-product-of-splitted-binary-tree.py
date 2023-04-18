# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        vals = []
        mod = 1000000007
        
        def fn(node): 
            """Return sum of sub-tree."""
            if not node: return 0 
            ans = node.val + fn(node.left) + fn(node.right)
            vals.append(ans)
            return ans
        total = fn(root)
        print(vals)
        return max((total-x)*x for x in vals) % mod