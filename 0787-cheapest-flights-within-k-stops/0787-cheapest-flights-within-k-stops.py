import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(dict)
        for a,b,c in flights:
            g[a][b]=c
        q = [(0,0,src)]
        visited = {}
        while q:
            p,s,n = heapq.heappop(q)
            if n== dst and s-1<=k:
                return p
            if n not in visited or visited[n]>s:
                visited[n]=s
                for nei,v in g[n].items():
                    heapq.heappush(q,(p+v,s+1,nei))
        return -1
        