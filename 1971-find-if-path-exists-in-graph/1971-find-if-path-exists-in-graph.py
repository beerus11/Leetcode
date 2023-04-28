class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        visited = set()
        def dfs(src,des):
            if src == des:
                return True
            visited.add(src)
            for nei in g[src]:
                if nei not in visited:
                    if dfs(nei,des):
                        return True
            return False
            
        return dfs(source,destination)
        