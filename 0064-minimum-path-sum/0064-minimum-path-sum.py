class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp = {}
        def mp(grid,i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i> len(grid)-1 or j> len(grid[0])-1:
                self.dp[(i,j)]= float('inf')
                return self.dp[(i,j)]
            if i == len(grid)-1 and j == len(grid[0])-1:
                self.dp[(i,j)] = grid[i][j]
                return self.dp[(i,j)]
            a = mp(grid,i,j+1)
            b = mp(grid,i+1,j)
            self.dp[(i,j)] = grid[i][j]+min(a,b)
            return self.dp[(i,j)]
        return mp(grid,0,0)
            
        