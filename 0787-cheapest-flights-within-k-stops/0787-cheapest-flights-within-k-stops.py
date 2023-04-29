import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(defaultdict)
        for a,b,c in flights:
            g[a][b]=c
            
        q = [(0,src,0)]
        visited = {}
        while q:
            cost,n,stops = heapq.heappop(q)
            #print(node,cost,count,node==dst,count<k)
            if n==dst and stops-1<=k:
                return cost
            if n not in visited or visited[n]>stops:
                visited[n]=stops
                for nei,p in g[n].items():
                        heapq.heappush(q,(cost+p,nei,stops+1))
        return -1
        