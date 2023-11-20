class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        t = 0
        cm = {k:Counter(list(g)) for k,g in enumerate(garbage)}
        last_seen = defaultdict(int)
        for i in range(len(garbage)):
            for c in ['G','P','M']:
                if c in cm[i]:
                    t+=cm[i][c]
                    last_seen[c]=i
        cost = []
        for tv in travel:
            if len(cost)==0:
                cost.append(tv)
            else:
                cost.append(cost[-1]+tv)
        for k,v in last_seen.items():
            if v>0:
                t+=cost[v-1]
            
        return t
        