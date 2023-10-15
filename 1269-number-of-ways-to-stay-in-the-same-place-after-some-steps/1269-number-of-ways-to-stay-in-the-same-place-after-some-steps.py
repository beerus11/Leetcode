class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M= 10**9 + 7
        @lru_cache(None)
        def nw(i,s):
            if i<0 or i==arrLen or s>steps:
                return 0
            if s==steps and i==0:
                return 1
            a=nw(i+1,s+1)%M
            b=nw(i-1,s+1)%M
            c=nw(i,s+1)%M
            return (a+b+c)%M
        return nw(0,0)