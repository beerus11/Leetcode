# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        def dfs(node,parent):
            if not node:
                return
            g[node].append(parent)
            g[parent].append(node)
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root.left,root)
        dfs(root.right,root)
        
        q = [(target,0)]
        ans = []
        visited = set()
        while q:
            n,c = q.pop(0)
            if c==k:
                ans.append(n.val)
            visited.add(n)
            for nei in g[n]:
                if nei not in visited:
                    q.append((nei,c+1))
        return ans
        
            
        