# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0
        def st(node):
            if not node:
                return 0
            if low<=node.val<=high:
                self.s+=node.val
            if node.val<= high:
                st(node.right)
            if node.val>=low:
                st(node.left)
        st(root)
        return self.s
                
        