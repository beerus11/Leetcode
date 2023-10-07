class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        M = 10**9 + 7
        @lru_cache(None)
        def dp(i,j,mx):
            if i==n:
                if j==0:
                    return 1
                return 0
            ans = mx*dp(i+1,j,mx)%M
            for a in range(mx+1,m+1):
                ans = (ans+dp(i+1,j-1,a))%M
            return ans
        return dp(0,k,0)
        