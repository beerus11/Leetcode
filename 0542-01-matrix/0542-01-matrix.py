class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [[float('inf')]*len(mat[0]) for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if j>0:
                        dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
                    if i>0:
                        dp[i][j] = min(dp[i-1][j]+1,dp[i][j])
                else:
                    dp[i][j] = 0
                    
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j]==1:
                    if j<len(mat[0])-1:
                        dp[i][j] = min(dp[i][j+1]+1,dp[i][j])
                    if i<len(mat)-1:
                        dp[i][j] = min(dp[i+1][j]+1,dp[i][j])
                else:
                    dp[i][j] = 0
        return dp
            