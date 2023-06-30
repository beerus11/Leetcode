# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [(root,0)]
        levels = defaultdict(list)
        while q:
            n,l = q.pop(0)
            levels[l].append(n.val)
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
        ans = []
        for k,v in levels.items():
            ans.append(sum(v)/len(v))
        return ans
        
            
        
        