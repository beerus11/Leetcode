class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:     
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        def mincost(node,parent):
            res = 0
            for nei in g[node]:
                if nei!=parent:
                    res+=mincost(nei,node)
            if node!=0:
                if hasApple[node] or res>0:
                    res+=2
            return res
        return mincost(0,None)
            
            
        