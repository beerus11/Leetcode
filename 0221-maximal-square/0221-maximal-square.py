class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mxs = 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0:
                    dp[i][j]= int(matrix[0][j])
                elif j==0:
                    dp[i][j] = int(matrix[i][0])
                elif matrix[i-1][j-1]!="0" and matrix[i][j]!="0" and matrix[i-1][j]!="0" and matrix[i][j-1]!="0" :
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                else:
                    dp[i][j] = int(matrix[i][j])
                mxs = max(mxs,dp[i][j])
        return mxs**2
                    
                    
                    
                    
                
            
        