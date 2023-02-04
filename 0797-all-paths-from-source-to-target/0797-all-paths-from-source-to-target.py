class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        def dfs(src,dest,path):
            if src==dest:
                self.ans.append(path)
            for i in graph[src]:
                path.append(i)
                dfs(i,dest,path[:])
                path.pop()
        dfs(0,len(graph)-1,[0])
        return self.ans
            
        