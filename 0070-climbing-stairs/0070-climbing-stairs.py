class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x):
            if x<=1:
                return x
            if x==2:
                return 2
            return dfs(x-1)+dfs(x-2)
        return dfs(n)