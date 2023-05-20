class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(i):
            if i>=0 and i<n:
                if i not in visited:
                    visited.add(i)
                    for k in range(n):
                        if i!=k and isConnected[i][k]==1:
                            dfs(k)
        count =0 
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
        