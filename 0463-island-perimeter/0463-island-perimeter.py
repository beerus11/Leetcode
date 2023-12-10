class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=1:
                    continue
                if i==0:
                    if j>0 and grid[i][j-1]==1:
                        count+=2
                    else:
                        count+=4
                elif j==0:
                    if grid[i-1][j]==1:
                        count+=2
                    else:
                        count+=4
                else:
                    count+=4
                    count-=grid[i][j-1]*2
                    count-=grid[i-1][j]*2
        return count
                    
        