# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [(root,0)]
        m = {}
        while q:
            n,l = q.pop(0)
            m[l]=n.val
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
        ans = [None]*len(m)
        for k,v in m.items():
            ans[k]=v
        return ans
                
        