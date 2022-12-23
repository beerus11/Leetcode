class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.dp = {}
        def up(grid,i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return 0
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if grid[i][j]==1:
                self.dp[(i,j)] = 0
                return self.dp[(i,j)]
            if i==len(grid)-1 and j==len(grid[0])-1:
                self.dp[(i,j)] = 1
                return self.dp[(i,j)]
            a = up(grid,i+1,j)
            b = up(grid,i,j+1)
            self.dp[(i,j)] =  a+b
            return self.dp[(i,j)]
        return up(obstacleGrid,0,0)
        