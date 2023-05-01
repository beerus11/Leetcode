class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def mps(i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            a = mps(i+1,j)
            b = mps(i,j+1)
            return grid[i][j]+min(a,b)
        return mps(0,0)
        