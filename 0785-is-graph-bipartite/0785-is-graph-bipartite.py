class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        def bfs(node,c):
            color[node]=0
            q = [node]
            while q:
                n = q.pop(0)
                for nei in graph[n]:
                    if color[nei]==color[n]:
                        return False
                    if color[nei]==-1:
                        color[nei] = 1^color[n]
                        q.append(nei)
            return True
                
        
        for i in range(len(graph)):
            if color[i]==-1:
                if not bfs(i,-1):
                    return False
        return True
        
        