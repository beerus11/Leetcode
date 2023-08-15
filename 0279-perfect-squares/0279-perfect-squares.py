import math
class Solution:
    def numSquares(self, n: int) -> int:
        arr = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')]*(n+1)
        dp[0]=0
        
        for i in range(1,n+1):
            for s in arr:
                if i <s:
                    break
                dp[i] = min(dp[i],dp[i-s]+1)
        return dp[-1]
        