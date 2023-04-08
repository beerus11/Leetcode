class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return [i for i in range(n)]
        
        g = defaultdict(set)
        
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            
        leaves = []
        for i in range(n):
            if len(g[i])==1:
                leaves.append(i)
                
        remaining_leaves = n
        
        while remaining_leaves >2:
            remaining_leaves -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                nei = g[leaf].pop()
                g[nei].remove(leaf)
                if len(g[nei])==1:
                    new_leaves.append(nei)
            leaves = new_leaves
            
        return leaves
                    
            
            