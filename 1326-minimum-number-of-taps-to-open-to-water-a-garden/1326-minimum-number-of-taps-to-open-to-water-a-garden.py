class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inf = int(1e9)
        dp = [inf]*(n+1)
        
        dp[0]=0
        for i in range(n+1):
            start = max(0,i-ranges[i])
            end = min(n,i+ranges[i])
            for j in range(start,end+1):
                dp[end]=min(dp[end],dp[j]+1)
        if dp[n]==inf:
            return -1
        
        return dp[n]
            
        