# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
 # handle case 1
        if root is None:
            return ''
        # we convert root.val to string here, then append results from different cases
        s = str(root.val)
        # handle case 2
        # this line is obviously not necessary
        if root.left is None and root.right is None:
            s += ''
        # handle case 3
        if root.left:
            s += '({})'.format(self.tree2str(root.left))
        # handle case 4
        # alternatively, you can use `elif root.right: s += '()'`
        if root.left is None and root.right:
            s += '()'
        # handle case 5
        if root.right:
            s += '({})'.format(self.tree2str(root.right))
        return s    
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root==None:
            return ""
        s = str(root.val)
        if root.left ==None and root.right==None:
            s+= ""
        if root.left:
            s+="({})".format(self.tree2str(root.left))
        if root.left ==None and root.right:
            s+="()"
        if root.right:
            s+="({})".format(self.tree2str(root.right))
        return s
            
        
        