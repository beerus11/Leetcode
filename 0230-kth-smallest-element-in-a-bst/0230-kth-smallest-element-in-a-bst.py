# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def dfs(node):
            if not node or len(self.arr)==k:
                return 
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
            
        dfs(root)
        print(self.arr)
        return self.arr[k-1]
        