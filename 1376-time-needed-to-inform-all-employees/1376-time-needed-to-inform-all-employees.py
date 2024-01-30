class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        
        for i in range(len(manager)):
            g[manager[i]].append(i)
            
        self.ans = float('-inf')
        def dfs(node,t):
            self.ans = max(self.ans,t)
            for nei in g[node]:
                dfs(nei,informTime[node]+t)
        
        dfs(headID,0)
        return self.ans
        
        