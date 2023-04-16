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
        
        seen_stops = set()
        seen_bus = set()
        while q:
            node,count = q.popleft()
            if node == target:
                return count
            for bus_no in g[node]:
                if bus_no not in seen_bus:
                    seen_bus.add(bus_no)
                    for stop in routes[bus_no]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            q.append((stop,count+1))
        return -1
                    
                
                
        