class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def msp(i,j):
            if i==len(grid) or j==len(grid[0]):
                return float('inf')
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[len(grid)-1][len(grid[0])-1]
            return grid[i][j]+min(msp(i+1,j),msp(i,j+1))
        return msp(0,0)
        