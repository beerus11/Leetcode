class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        def bfs(i,j):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1:
                return
            if grid[i][j]=="0":
                return
            grid[i][j]="0"
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                bfs(i+a,j+b)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        return count