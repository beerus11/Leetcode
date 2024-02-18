class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        
        for s,score in items:
            heappush(g[s],score)
            if len(g[s])>5:
                heappop(g[s])
        ans = []
        
        for k,v in g.items():
            ans.append([k,sum(v)//len(v)])
        ans.sort()
        return ans
                
        