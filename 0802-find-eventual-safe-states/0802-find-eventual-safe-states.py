class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        W,G,B = 0,1,2
        colors = defaultdict(int)
        def dfs(node):
            if colors[node]!=W:
                return colors[node]==B
            colors[node]=G
            for nei in graph[node]:
                if colors[nei]==B:
                    continue
                if colors[nei]==G or not dfs(nei):
                    return False
            colors[node]=B
            return True
        
        return list(filter(dfs,range(len(graph))))
        