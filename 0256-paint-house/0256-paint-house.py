class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def ph(col,i):
            if i== len(costs):
                return 0
            a = costs[i][0]+ph(0,i+1)
            b = costs[i][1]+ph(1,i+1)
            c = costs[i][2]+ph(2,i+1)
            if col==-1:
                return min([a,b,c])
            if col==0:
                return min(b,c)
            if col==1:
                return min(a,c)
            return min(a,b)
        return ph(-1,0)
        