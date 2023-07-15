# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m = defaultdict(int)
        
        q = [(root,1)]
        
        while q:
            node,level = q.pop(0)
            m[level]+=node.val
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        mxv = max(m.values())
        
        for k in sorted(m.keys()):
            if m[k]==mxv:
                return k
        return -1
                
            
            
        