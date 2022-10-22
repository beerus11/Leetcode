from collections import defaultdict
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
        q = [k]
        
        while q:
            node = q.pop(0)
            if node not in self.g:
                continue

            for nei,nei_time in self.g[node].items():
                arrival_time = self.signal[node] + nei_time
                if self.signal[nei]> arrival_time:
                    self.signal[nei] = arrival_time
                    q.append(nei)
                             
        m = max(self.signal[1:])
        if m==float('inf'):
            return -1
        return m