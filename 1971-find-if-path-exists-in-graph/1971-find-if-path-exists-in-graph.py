class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(list)
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visited = set()
        def dfs(node,dest):
            if node == dest :
                return True
            visited.add(node)
            for nei in g[node]:
                if nei not in visited:
                    if dfs(nei,dest):
                        return True
            return False
        return dfs(source,destination)
        