class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        self.count = 0
        for a,b in connections:
            g[a].append((b,1))
            g[b].append((a,0))
            
        def dfs(node,parent):
            if node not in g:
                return
            for nei in g[node]:
                if nei[0]!=parent:
                    self.count+=nei[1]
                    dfs(nei[0],node)
        dfs(0,-1)
        return self.count
                    
        