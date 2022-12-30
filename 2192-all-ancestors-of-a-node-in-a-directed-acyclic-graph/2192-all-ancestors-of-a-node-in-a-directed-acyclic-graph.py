from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        
        graph = defaultdict(list)
        for f, t in edges:
            graph[t].append(f)
        
        memo = defaultdict(list)
        def dfs(src):
            if src in memo:
                return memo[src]
            
            for nei in graph[src]:
                memo[src] += [nei]+dfs(nei)
            
            memo[src] = list(set(memo[src]))
            return memo[src]
        
        for i in range(n):
            dfs(i)
        return [sorted(memo[i]) for i in range(n)]