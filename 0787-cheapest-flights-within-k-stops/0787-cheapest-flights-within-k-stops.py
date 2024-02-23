class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for a,b,c in flights:
            g[a].append((b,c))
            
        q = [(0,src,0)]
        v = {}
        
        while q:
            cost,node,stops = heappop(q)
            if node==dst:
                return cost
            if stops>k or (node in v and v[node]<stops):
                continue
            v[node]=stops
            for nei,c in g[node]:
                heappush(q,(cost+c,nei,stops+1))
        return -1
        
            
            
        