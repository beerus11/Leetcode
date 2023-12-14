class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        col,row = defaultdict(defaultdict),defaultdict(defaultdict)
        
        diff = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 0 not in col[j]:
                    col[j][0]=0
                if 1 not in col[j]:
                    col[j][1]=0
                if 0 not in row[i]:
                    row[i][0]=0
                if 1 not in row[i]:
                    row[i][1]=0
                col[j][0]+=1^grid[i][j]
                col[j][1]+=grid[i][j]
                row[i][0]+=1^grid[i][j]
                row[i][1]+=grid[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j]=(row[i][1]+col[j][1]-col[j][0]-row[i][0])
        return diff