class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph)-1
        def dfs(node,path):
            if node==None:
                return
            if node==target:
                ans.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei,path)
                path.pop()
        dfs(0,[0])
        return ans
            
        