class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        to=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    to+=1
                elif grid[i][j]==2:
                    to+=1
                    q.append((i,j,0))
        if to==0:
            return 0
        count = 0
        mxt = -1
        while q:
            i,j,t = q.pop(0)
            print(i,j,t)
            if grid[i][j]==0:
                continue
            count+=1
            mxt = max(mxt,t)
            grid[i][j]=0
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+a,j+b
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1:
                    q.append((x,y,t+1))
        if count ==to:
            return mxt
        return -1