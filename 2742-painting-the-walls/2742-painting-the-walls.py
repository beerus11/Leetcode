class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def mc(i,r):
            if r<=0:
                return 0
            if i==len(cost):
                return float('inf')
            pick = cost[i]+mc(i+1,r-time[i]-1)
            not_pick = mc(i+1,r)
            return min(pick,not_pick)
        return mc(0,len(cost))
            
            
        