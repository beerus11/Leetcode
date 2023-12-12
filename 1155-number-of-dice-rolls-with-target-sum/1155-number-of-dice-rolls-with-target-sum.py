class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10**9+7
        @lru_cache(None)
        def dfs(left,sum_left):
            if left==0 and sum_left==0:
                return 1
            if left<0 or sum_left<0:
                return 0
            res = 0
            for i in range(1,k+1):
                res+=dfs(left-1,sum_left-i)
            return res%M
        return dfs(n,target)
        