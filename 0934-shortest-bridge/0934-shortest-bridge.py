from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque([])
        def dfs(i,j):
            if grid[i][j]==0:
                return
            grid[i][j]=-1
            q.append((i,j,0))
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+a,j+b
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1:
                    dfs(x,y)
        run = True            
        for i in range(len(grid)):
            if not run:
                break
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dfs(i,j)
                    run = False
                    break
                    
        while q:
            i,j,k = q.popleft()
            if grid[i][j]==1:
                return k-1
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+a,j+b
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]):
                    if grid[x][y]==1:
                        return k
                    elif grid[x][y]==0:
                        q.append((x,y,k+1))
                        grid[x][y]=-1
        return -1
            
            
        
        