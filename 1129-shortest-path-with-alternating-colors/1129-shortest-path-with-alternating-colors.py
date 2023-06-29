class Solution:
    def shortestAlternatingPaths(self, node: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        
        for a,b in redEdges:
            g[a].append((b,'r'))
        
        for a,b in blueEdges:
            g[a].append((b,'b'))
            
        q = [(0,0,-1)]
        visited = set()
        ans = [-1]*(node)
        ans[0]=0
        visited.add((0,'r'))
        visited.add((0,'b'))
        
        while q:
            n,l,pc = q.pop(0)
            for nei,c in g[n]:
                if (nei,c) not in visited and pc!=c:
                    if ans[nei]==-1:
                        ans[nei]=1+l
                    visited.add((nei,c))
                    q.append((nei,l+1,c))
        return ans
        