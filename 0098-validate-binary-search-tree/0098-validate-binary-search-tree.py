# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node,mn,mx):
            if node==None:
                return True
            if node.val<=mn:
                return False
            if node.val>=mx:
                return False
            return isBST(node.left,mn,node.val) and isBST(node.right,node.val,mx)
        return isBST(root,float('-inf'),float('inf'))