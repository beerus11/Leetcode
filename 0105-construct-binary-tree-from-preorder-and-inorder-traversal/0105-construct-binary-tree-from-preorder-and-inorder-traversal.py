# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm= {}
        for k,v in enumerate(inorder):
            hm[v]=k
        
        self.po_index = 0
        def build(l,r):
            if l>r:
                return None
            root = TreeNode(preorder[self.po_index])
            index = hm[preorder[self.po_index]]
            
            self.po_index+=1
            
            root.left = build(l,index-1)
            root.right = build(index+1,r)
            
            return root
        return build(0,len(inorder)-1)