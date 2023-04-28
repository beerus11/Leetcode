class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b,c in roads:
            g[a].append((b,c))
            g[b].append((a,c))
        
        visited = set()
        def bfs(node):
            ans = float('inf')
            q = [node]
            while q:
                x = q.pop(0)
                for nei,v in g[x]:
                    ans = min(ans,v)
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return ans
                    
                    
        return bfs(1)
        