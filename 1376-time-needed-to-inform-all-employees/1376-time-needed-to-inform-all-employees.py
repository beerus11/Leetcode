class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        self.mxt = float('-inf')
        
        for i in range(len(manager)):
            if manager[i]!=-1:
                g[manager[i]].append(i)
        
        def dfs(node,t):
            self.mxt = max(self.mxt,t)
            for nei in g[node]:
                dfs(nei,t+informTime[node])
        dfs(headID,0)
        return self.mxt
        