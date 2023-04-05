class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {}
        def up(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i==m-1 and j ==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            a = up(i+1,j)
            b = up(i,j+1)
            self.dp[(i,j)]=a+b
            return self.dp[(i,j)]
        return up(0,0)
            
        