class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                elif grid[i][j]==2:
                    q.append((i,j,0))
                    count+=1
                    
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        t = 0
        while q:
            i,j,t = q.pop(0)
            count-=1
            for a,b in dirs:
                x,y = a+i,b+j
                if x>=0 and y>=0 and x<len(grid) and y <len(grid[0]) and grid[x][y]==1:
                    grid[x][y]=2
                    q.append((x,y,t+1))
                    
                    
        return  t if count==0 else -1
                    
            