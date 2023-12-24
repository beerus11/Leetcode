# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
            if l>r:
                return None
            v = postorder.pop()
            node = TreeNode(v)
            
            idx = hm[v]
            node.right =helper(idx+1,r)
            node.left=helper(l,idx-1)
            return node
            
        hm = {v:i for i,v in enumerate(inorder)}
        return helper(0,len(inorder)-1)
        