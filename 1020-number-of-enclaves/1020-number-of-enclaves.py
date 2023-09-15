class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        v = set()
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0 or (i,j) in v:
                return
            v.add((i,j))
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y =i+a,j+b
                dfs(x,y)
            return
        
        for i in range(m):
            if grid[i][0]==1 and (i,0) not in v:
                dfs(i,0)
            if grid[i][n-1]==1 and (i,n-1) not in v:
                dfs(i,n-1)
                
        for i in range(n):
            if grid[0][i]==1 and (0,i) not in v:
                dfs(0,i)
            if grid[m-1][i]==1 and (m-1,i) not in v:
                dfs(m-1,i)
                
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in v:
                    count+=1
        return count
            