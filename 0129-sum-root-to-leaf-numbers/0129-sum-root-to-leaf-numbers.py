# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,arr=[]):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
            if not node.left and not node.right:
                x = "".join(map(str,arr))
                self.ans+=int(x)
                arr.pop()
            elif len(arr)>0:
                arr.pop()
        dfs(root)
        return self.ans
            