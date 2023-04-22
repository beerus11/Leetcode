class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node,path):
            if node == len(graph)-1:
                ans.append(path[:])
                return
            for nn in graph[node]:
                path.append(nn)
                dfs(nn,path)
                path.pop()
        
        path = [0]
        dfs(0,path)
        return ans