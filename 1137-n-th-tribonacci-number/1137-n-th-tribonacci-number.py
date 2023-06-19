class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def t(x):
            if x<=1:
                return x
            if x==2:
                return 1
            return t(x-1)+t(x-2)+t(x-3)
        return t(n)
        