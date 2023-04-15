class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def climb(i):
            if i ==1:
                return 1
            if i==2:
                return 2
            return climb(i-1)+climb(i-2)
        return climb(n)