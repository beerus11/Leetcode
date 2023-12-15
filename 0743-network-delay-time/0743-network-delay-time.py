class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(defaultdict)
        
        for a,b,c in times:
            g[a][b]=c
            
        q = [(k,0)]
        hm = {i:float('inf') for i in range(1,n+1)}
        while q:
            node,t = heapq.heappop(q)
            if t>=hm[node]:
                continue
            hm[node]=t
            for nei,time in g[node].items():
                q.append((nei,t+time))
        ans = max([v for k,v in hm.items()])
        if ans==float('inf'):
            return -1
        return ans
                
        
            
        
        