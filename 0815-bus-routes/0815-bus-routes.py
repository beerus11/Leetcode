from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        g = defaultdict(list)
        
        for k,v in enumerate(routes):
            for r in v:
                g[r].append(k)
        q = deque([(source,0)])
        
        bus_seen = set()
        stop_seen = set()
        while q:
            s,c= q.popleft()
            if s == target:
                return c
            for r in g[s]:
                if r not in bus_seen:
                    bus_seen.add(r)
                    for stop in routes[r]:
                        if stop not in stop_seen:
                            stop_seen.add(stop)
                            q.append((stop,c+1))
        return -1
                            
                
                
                
                
        