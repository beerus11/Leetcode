class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="*":
                    q.append((i,j,0))
        if len(q)==0:
            return -1
        c = 0            
        while q:
            i,j,d = q.pop(0)
            for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                x,y = i+a,j+b
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]!="X":
                    if grid[x][y]=="#":
                        return d+1
                    q.append((x,y,d+1))
                    grid[x][y]="X"
        return -1
                    
        