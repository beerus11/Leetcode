# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node,mx,mn):
            if not node:
                return True
            if node.val>=mx or node.val<=mn:
                return False
            
            return isBST(node.left,node.val,mn) and isBST(node.right,mx,node.val)
        return isBST(root,float('inf'),-1*float('inf'))
        
        