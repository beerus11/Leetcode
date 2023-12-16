class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return 0
        M = 2*(10**9)
        self.dp = {}
        def dfs(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i>=len(grid) or j>=len(grid[0]) or grid[i][j]==1:
                return 0
            print(i,j)
            if i==len(grid)-1 and j==len(grid[0])-1:
                return 1
            self.dp[(i,j)] = dfs(i+1,j)+dfs(i,j+1)%M
            return self.dp[(i,j)]
        return dfs(0,0)
        