# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            self.ans.append(root.val)
        dfs(root)
        return self.ans
        