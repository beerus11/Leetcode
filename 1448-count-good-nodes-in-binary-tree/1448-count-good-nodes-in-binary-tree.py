# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count =0
        def gn(node,mx):
            if not node:
                return
            if node.val>=mx:
                self.count+=1
            mx = max(mx,node.val)
            gn(node.left,mx)
            gn(node.right,mx)
        gn(root,float('-inf'))
        return self.count