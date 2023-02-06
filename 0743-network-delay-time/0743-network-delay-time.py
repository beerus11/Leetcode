from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(dict)
        
        for s,d,t in times:
            g[s][d]=t
        signalRcvd = [float('inf')]*(n+1)
        signalRcvd[0]=0
        signalRcvd[k]=0
        q = [(k,0)]
        while q:
            n,t = heapq.heappop(q)
            if t> signalRcvd[n]:
                continue
            for nei,v in g[n].items():
                if signalRcvd[nei]>t+v:
                    signalRcvd[nei] = t+v
                    heapq.heappush(q,(nei,t+v))
        mx = max(signalRcvd)
        print(signalRcvd)
        return mx if mx!=float('inf') else -1