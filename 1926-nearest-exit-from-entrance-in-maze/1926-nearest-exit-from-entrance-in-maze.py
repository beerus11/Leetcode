class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m = entrance[0],entrance[1]
        if maze[n][m]=="+":
                return -1
        q = [(entrance[0],entrance[1],0)]
        visited = set()
        min_steps = float('inf')
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            a,b,s = q.pop(0)
            if not(a==n and b==m) and (a==0 or b==0 or a==len(maze)-1 or b==len(maze[0])-1):
                min_steps = min(min_steps,s)
                continue
            if s>min_steps:
                continue
            for d in dirs:
                x,y = a+d[0],b+d[1]
                if x>=0 and y>=0 and x<=len(maze)-1 and y<=len(maze[0])-1 and maze[x][y]==".":
                    maze[x][y]="+"
                    q.append((x,y,s+1))
        return min_steps if min_steps != float('inf') else -1
                
            
                
            
        