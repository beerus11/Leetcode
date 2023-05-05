class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.dp = {}
        def dfs(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if j<0 or j>=len(matrix):
                self.dp[(i,j)] = float('inf')
                return self.dp[(i,j)]
            if i==len(matrix)-1:
                self.dp[(i,j)]= matrix[i][j]
                return self.dp[(i,j)]
            a = dfs(i+1,j)     
            b = dfs(i+1,j-1)
            c = dfs(i+1,j+1)
            self.dp[(i,j)] = min([a,b,c])+matrix[i][j]
            return self.dp[(i,j)]
        return min([dfs(0,i) for i in range(len(matrix))])