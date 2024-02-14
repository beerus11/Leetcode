class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)
        
        def dist(a,b,c,d):
            return (a-c)**2 + (b-d)**2
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i==j:
                    continue
                a,b,r1 = bombs[i]
                c,d,r2 = bombs[j]
                distance = dist(a,b,c,d)
                if distance<=r1**2:
                    g[i].append(j)
                    
        def bfs(node):
            q = deque([node])
            v = set([node])
            while q:
                n = q.popleft()
                for nei in g[n]:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
            return len(v)
                        
                    
        mx = 0            
        for i in range(len(bombs)):
            mx = max(mx,bfs(i))
        return mx
        