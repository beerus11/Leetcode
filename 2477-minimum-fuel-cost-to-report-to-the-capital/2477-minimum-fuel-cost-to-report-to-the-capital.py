class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = defaultdict(list)
        for a,b in roads:
            g[a].append(b)
            g[b].append(a)
        self.res = 0
        def dfs(node,parent):
            passengers = 0
            for child in g[node]:
                if child!=parent:
                    p=dfs(child,node)
                    passengers+=p
                    self.res+=int(ceil(p/seats))
            return passengers+1
                    
        dfs(0,-1)
        return self.res
            