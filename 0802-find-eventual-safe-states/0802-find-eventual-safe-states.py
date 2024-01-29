class Solution:
    def dfs(self,node):
        if node in self.stack:
            return True
        if node in self.visited:
            return False
        self.visited.add(node)
        self.stack.add(node)
        
        for nei in self.graph[node]:
            if self.dfs(nei):
                return True
        self.stack.remove(node)
        return False
            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.visited = set()
        self.stack = set()
        self.graph = graph
        
        self.v = len(graph)
        
        for i in range(self.v):
            self.dfs(i)
            
        ans = []
        for i in range(self.v):
            if i not in self.stack:
                ans.append(i)
        
        return ans