class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @lru_cache(None)
        def ms(i,j):
            if i==n:
                return 0
            if j==n or j==-1:
                return float('inf')
            a = ms(i+1,j-1)
            b = ms(i+1,j)
            c = ms(i+1,j+1)
            return matrix[i][j]+min(a,b,c)
        ans = float('inf')
        for i in range(len(matrix)):
            a = ms(1,i-1)
            b = ms(1,i)
            c = ms(1,i+1)
            ans = min(ans,matrix[0][i]+min([a,b,c]))
        return ans
            
        