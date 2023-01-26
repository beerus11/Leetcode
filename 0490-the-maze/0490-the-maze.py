class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        def dfs(m,i,j,dest):
            if (i,j) in visited:
                return False
            else:
                visited.add((i,j))
            if i==dest[0] and j == dest[1]:
                return True
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i,j
                while 0<=x+a<len(m) and 0<=y+b<len(m[0]) and m[x+a][y+b]!=1:
                    x+=a
                    y+=b
                if dfs(m,x,y,dest):
                    return True
            return False
        return dfs(maze,start[0],start[1],destination)