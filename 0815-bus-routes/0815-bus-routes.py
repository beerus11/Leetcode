class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        g = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                g[routes[i][j]].append(i)
                
        
        q = deque([(source,0)])
        stop_seen = set()
        route_seen = set()
        
        while q:
            stop,cnt = q.popleft()
            if stop==target:
                return cnt
            for r in g[stop]:
                if r in route_seen:
                    continue
                route_seen.add(r)
                for s in routes[r]:
                    if s in stop_seen:
                        continue
                    stop_seen.add(s)
                    q.append((s,cnt+1))
                    
            
        return -1
        