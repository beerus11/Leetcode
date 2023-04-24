from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        if grid[len(grid)-1][len(grid[0])-1]==1:
            return -1
        if len(grid)==1 and len(grid[0])==1:
            return 1 if grid[0][0]==0 else -1
        q = deque([(0,0,1)])
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        while q:
            i,j,l = q.popleft()
            for a,b in dirs:
                x,y=i+a,j+b
                if x==len(grid)-1 and y==len(grid[0])-1:
                    return l+1
                if x == -1 or x == len(grid) or y == -1 or y == len(grid[0]) or grid[x][y]:
                    continue
                grid[x][y] = 1
                q.append((x, y, l + 1))
        return -1
        
                
        