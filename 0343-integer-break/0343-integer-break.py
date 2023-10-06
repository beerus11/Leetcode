class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def maxP(x):
            if x==1:
                return 1
            mxp = 1
            for i in range(1,x):
                a = i*maxP(x-i)
                b = i*(x-i)
                mxp = max(mxp,max(a,b))
            return mxp
        return maxP(n)
                
        