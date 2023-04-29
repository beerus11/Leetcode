class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        g = defaultdict(list)
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in g[node]:
                if nei not in visited:
                    dfs(nei)
                    
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count-1
            
        