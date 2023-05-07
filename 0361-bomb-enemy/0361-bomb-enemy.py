class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        rows,cols= len(grid),len(grid[0])
        
        max_counts = 0
        rc = 0
        cc = [0]*cols
        for r in range(rows):
            for c in range(cols):
                if c==0 or grid[r][c-1]=="W":
                    rc=0
                    for k in range(c,cols):
                        if grid[r][k]=="W":
                            break
                        elif grid[r][k]=="E":
                            rc+=1
                if r==0 or grid[r-1][c]=="W":
                    cc[c]=0
                    for k in range(r,rows):
                        if grid[k][c]=="W":
                            break
                        elif grid[k][c]=="E":
                            cc[c]+=1
                if grid[r][c]=="0":
                    max_counts= max(max_counts,rc+cc[c])
                
        return max_counts
                
        