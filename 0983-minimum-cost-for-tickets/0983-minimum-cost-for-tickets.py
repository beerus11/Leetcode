from collections import defaultdict
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        s = set(days)
        @lru_cache(None)
        def mc(i):
            if i>days[-1]:
                return 0
            if i in s:
                a = costs[0]+mc(i+1)
                b = costs[1]+mc(i+7)
                c = costs[2]+mc(i+30)
                return min([a,b,c])
            else:
                return mc(i+1)
        return mc(0)
            
        