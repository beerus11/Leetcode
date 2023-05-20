class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        if g[0][0]==1 or g[len(g)-1][len(g[0])-1]==1:
            return 0
        self.dp = {}
        def up(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i==len(g) or j ==len(g[0]):
                return 0
            if i==len(g)-1 and j==len(g[0])-1:
                return 1
            if g[i][j]==1:
                return 0
            self.dp[(i,j)]=up(i+1,j) + up(i,j+1)
            return self.dp[(i,j)]
        return up(0,0)
        