from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        self.g = defaultdict(defaultdict)
        for a,b,c in times:
            self.g[a][b] = c
            
        self.signal = [float('inf')]*(n+1)
        
        self.signal[k]=0
        heap = [(0,k)]
        
        while heap:
            current_time,node = heapq.heappop(heap)
            if current_time>self.signal[node]:
                continue
            if node not in self.g:
                continue

            for nei,nei_time in self.g[node].items():
                arrival_time = current_time + nei_time
                if self.signal[nei]> arrival_time:
                    self.signal[nei] = arrival_time
                    heapq.heappush(heap,(arrival_time,nei))
                             
        m = max(self.signal[1:])
        if m==float('inf'):
            return -1
        return m