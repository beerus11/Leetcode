class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost)
        @lru_cache(None)
        def mc(i):
            if i<=1:
                return 0
            return min(cost[i-1]+mc(i-1),cost[i-2]+mc(i-2))
        return mc(len(cost))
                