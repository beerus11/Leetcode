# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        self.parent = {}
        def dfs(node,parent=None):
            if not node:
                return
            self.parent[node]=parent
            dfs(node.left,node)
            dfs(node.right,node)
            
        dfs(root)
        
        q = [(target,0)]
        visited = set()
        
        while q:
            n,d = q.pop(0)
            
            if n in visited:
                continue
            
            if d == k:
                self.ans.append(n.val)
                
            if n.left:
                q.append((n.left,d+1))
            if n.right:
                q.append((n.right,d+1))  
            if self.parent[n]:
                q.append((self.parent[n],d+1))
            visited.add(n)
        return self.ans
            
            
        
        