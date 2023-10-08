class Solution:
    def numTilings(self, n: int) -> int:
        M = 10**9 +7
        dp = [1, 2, 5]
        for i in range(3, n):
            dp.append((dp[i - 1] * 2 + dp[i - 3]) % M)
        return dp[n - 1]
        
        