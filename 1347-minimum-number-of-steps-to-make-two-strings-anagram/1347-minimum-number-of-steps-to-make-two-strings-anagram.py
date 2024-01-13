class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hm = Counter(s)
        for i in t:
            if i in t:
                hm[i]-=1
            else:
                hm[i]=-1
        ans = 0
        for k,v in hm.items():
            if v>0:
                ans+=v
        return ans
        