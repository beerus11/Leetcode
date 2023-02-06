from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        g = defaultdict(set)
        
        for i,v in enumerate(routes):
            for s in v:
                g[s].add(i)
        
        q = [(source,0)]
        
        seen_stops,seen_bus= set(),set()
        while q:
            s,c= q.pop(0)
            if s==target:
                return c
            for bus_no in g[s]:
                if bus_no not in seen_bus:
                    seen_bus.add(bus_no)
                    for stop in routes[bus_no]:
                        if stop not in seen_stops:
                            q.append((stop,c+1))
        return -1
            