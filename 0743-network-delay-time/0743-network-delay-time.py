class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(defaultdict)
        
        for a,b,c in times:
            g[a][b] = c
            
        q = [(k,0)]
        m = {k:0}
        while q:
            node,t = q.pop(0)
            for nei,v in g[node].items():
                x = v+t
                if (nei not in m) or x < m[nei]:
                    m[nei]=x
                    q.append((nei,x))
        #print(m)
        if len(m)<n:
            return -1
        return max([v for k,v in m.items()])
                
        
            
        
        