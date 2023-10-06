class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def maxP(x):
            if x==1:
                return 1
            mxp = 1
            for i in range(1,x):
                mxp = max(mxp,max(i*maxP(x-i),i*(x-i)))
            return mxp
        return maxP(n)
                
        