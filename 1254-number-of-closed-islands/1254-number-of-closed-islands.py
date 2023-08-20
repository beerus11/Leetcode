class Solution:
    def bfs(self,i,j):
        q = []
        q.append((i,j))
        self.visited.add((i,j))
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        closed = True
        
        while q:
            x,y = q.pop(0)
            for ind in range(4):
                a,b = dirs[ind]
                r,c = x+a,y+b
                if c<0 or r<0 or r>=len(self.grid) or c>=len(self.grid[0]):
                    closed = False
                elif self.grid[r][c]==0 and (r,c) not in self.visited:
                    q.append((r,c))
                    self.visited.add((r,c))
        return closed
            
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.grid = grid
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j]==0 and (i,j) not in self.visited and self.bfs(i,j):
                    count+=1
                    
        return count
        