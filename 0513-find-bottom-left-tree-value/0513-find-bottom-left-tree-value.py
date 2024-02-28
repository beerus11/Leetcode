# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [(0,root)]
        hm = defaultdict(list)
        mxl = -1
        while q:
            l,node = q.pop(0)
            mxl = max(mxl,l)
            if l-1 in hm:
                del hm[l-1]
            hm[l].append(node.val)
            if node.left:
                q.append((l+1,node.left))
            if node.right:
                q.append((l+1,node.right))
        return hm[mxl][0]
        