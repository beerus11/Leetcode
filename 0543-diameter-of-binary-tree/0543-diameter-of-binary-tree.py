# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            if node.left==None and node.right==None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            z = left+right
            if not node.left or not node.right:
                z+=1
            else:
                z+=2
            self.ans = max(self.ans,max([z,left,right]))
            
            return 1+max(left,right)
        dfs(root)
        return self.ans
        