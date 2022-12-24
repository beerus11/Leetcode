from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        def dfs(src,dest):
            if src not in seen:
                seen.add(src)
                if src==dest:
                    return True
                return any([dfs(nei,dest) for nei in graph[src]])
            
        
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)