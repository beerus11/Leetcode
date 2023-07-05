from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.q = deque()
        vis = set()
        def dfs(i,j,no):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid) or grid[i][j]==0 or (i,j) in vis:
                return
            vis.add((i,j))
            grid[i][j]=no
            self.q.append((i,j,0))
            dfs(i+1,j,no)
            dfs(i,j+1,no)
            dfs(i-1,j,no)
            dfs(i,j-1,no)
        
        def mark_one():
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j]==1:
                        dfs(i,j,0)
                        return
        mark_one()
        #print(grid,self.q)
        q = self.q
        visited = set()
        while q:
            i,j,l = q.popleft()
            for a,b in [[1,0],[0,1],[-1,0],[0,-1]]:
                x,y=a+i,b+j
                if x>=0 and y>=0 and x<len(grid) and y<len(grid):
                    if grid[x][y]==1:
                        return l
                    elif grid[x][y]==0 :
                        q.append((x,y,l+1))
                        grid[x][y]=-1
        return -1
        