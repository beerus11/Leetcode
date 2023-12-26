class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    visited[i][j]=1
                    q.append((i,j))
        distance = -1
        while q:
            s = len(q)
            while s>0:
                i,j = q.pop(0)
                for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                    x,y = i+a,j+b
                    if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and visited[x][y]==0:
                        q.append((x,y))
                        visited[x][y]=1
                s-=1
            distance+=1
        if distance<=0:
            return -1
        return distance
            
                    
        
        