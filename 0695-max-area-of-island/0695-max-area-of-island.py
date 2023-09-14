class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        v = set()
        def dfs(i,j):
            if (i,j) in v:
                return 0
            if grid[i][j]==0:
                return 0
            v.add((i,j))
            total = 1
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = i+a,j+b
                if x>=0 and y>=0 and x<m and y<n:
                    total+=dfs(x,y)
            return total
        mx = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in v:
                    mx= max(mx,dfs(i,j))
        return mx
                