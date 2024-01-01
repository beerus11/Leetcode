class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def mc(i,a,b):
            if a==0 and b==0:
                return 0
            if i==len(costs):
                return 0
            x,y=float('inf'),float('inf')
            if a>0:
                x = costs[i][0]+mc(i+1,a-1,b)
            if b>0:
                y = costs[i][1]+mc(i+1,a,b-1)
            return min(x,y)
        return mc(0,len(costs)//2,len(costs)//2)
        