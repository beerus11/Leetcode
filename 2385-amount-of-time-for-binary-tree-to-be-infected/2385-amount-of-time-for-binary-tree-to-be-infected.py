# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        def dfs(node):
            if not node:
                return
            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        q = [(start,0)]
        seen = set([start])
        mxt = -1
        while q:
            node,t = q.pop(0)
            mxt = max(mxt,t)
            for nei in g[node]:
                if nei not in seen:
                    q.append([nei,t+1])
                    seen.add(nei)
        return mxt
            
            
        