class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], dest: List[int]) -> bool:
        v = set()
        def dfs(i,j):
            if (i,j) in v:
                return False
            
            if i==dest[0] and j==dest[1]:
                return True
            
            v.add((i,j))
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = i,j
                while x+a>=0 and y+b>=0 and x+a<len(maze) and y+b <len(maze[0]) and maze[x+a][y+b]!=1:
                    x+=a
                    y+=b
                if dfs(x,y):
                    return True
            return False
        return dfs(start[0],start[1])
            