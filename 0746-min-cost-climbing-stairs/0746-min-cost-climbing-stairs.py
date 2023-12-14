class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def mc(i):
            if i>=len(cost)-2:
                return cost[i]
            return cost[i]+min(mc(i+1),mc(i+2))
        return min(mc(0),mc(1))
                