class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)
        
        n = len(bombs)
        
        for i in range(n):
            xi,yi,ri = bombs[i]
            for j in range(n):
                if i==j:
                    continue
                xj,yj,_= bombs[j]
                if ri**2 >= (xi-xj)**2 + (yi-yj)**2 :
                    g[i].append(j)
        def dfs(cur,visited):
            visited.add(cur)
            for nei in g[cur]:
                if nei not in visited:
                    dfs(nei,visited)
            return len(visited)
        
        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans,dfs(i,visited))
            
        return ans