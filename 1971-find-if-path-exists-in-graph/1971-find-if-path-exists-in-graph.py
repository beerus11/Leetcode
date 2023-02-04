from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        visited = set()
        def exists(src):
            if src == destination:
                return True
            if src in visited:
                return False
            visited.add(src)
            for nei in g[src]:
                if exists(nei):
                    return True
            return False
        return exists(source)