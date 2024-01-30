class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        w = []
        hm = defaultdict(int)
        ans = 0
        for k,v in enumerate(fruits):
            hm[v]+=1
            w.append(v)
            while len(hm)>2:
                e = w.pop(0)
                hm[e]-=1
                if hm[e]==0:
                    del hm[e]
            ans = max(ans,len(w))
        return ans
            