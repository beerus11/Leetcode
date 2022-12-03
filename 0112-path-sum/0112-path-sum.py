# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return
        if targetSum==root.val and not root.left and not root.right:
            return True
        if not root.left and not root.right:
            return False
            
        a = self.hasPathSum(root.left,targetSum-root.val)
        b = self.hasPathSum(root.right,targetSum-root.val)
        
        return a or b