class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    q.append([i, j, 0])
        ans = 0
        while(q):
            i,j,t = q.pop(0)
            ans = t
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ni, nj = i+x, j+y
                if(0<=ni<m and 0<=nj<n and grid[ni][nj] == 1):
                    grid[ni][nj] = 2
                    q.append([ni, nj, t+1])
        for row in grid:
            if(1 in row):
                return -1
        return ans
                    