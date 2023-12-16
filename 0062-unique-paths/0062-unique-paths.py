class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {}
        def dfs(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i>=m or j>=n:
                return 0
            if i==m-1 and j ==n-1:
                return 1
            self.dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return self.dp[(i,j)]
        return dfs(0,0)

            
        