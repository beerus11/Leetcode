class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node):
            self.visited.add(node)
            nei = edges[node]
            if nei == -1:
                return
            if nei not in self.visited:
                self.dist[nei]= self.dist[node]+1
                dfs(nei)
            elif nei in self.dist:
                self.ans = max(self.ans,self.dist[node]-self.dist[nei]+1)
            
        
        self.visited = set()
        self.dist = {}
        self.ans = -1
        for i in range(len(edges)):
            if i not in self.visited:
                self.dist = {}
                self.dist[i]=1
                dfs(i)
        return self.ans
            
        