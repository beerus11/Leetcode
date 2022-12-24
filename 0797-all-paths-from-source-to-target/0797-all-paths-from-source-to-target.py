class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        self.ans = []
        self.path = [0]
        def dfs(src,dest):
            if src==dest:
                self.ans.append(self.path[:])
                return
            for nei in graph[src]:
                self.path.append(nei)
                dfs(nei,dest)
                self.path.pop()
        dfs(0,len(graph)-1)
        return self.ans
        