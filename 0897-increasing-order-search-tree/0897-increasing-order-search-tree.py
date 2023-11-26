# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = TreeNode(0)
        self.next = ans
        def io(node):
            if not node:
                return
            io(node.left)
            self.next.right = TreeNode(node.val)
            self.next = self.next.right
            io(node.right)
        io(root)
        return ans.right
            
        