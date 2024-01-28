class Solution:
    def characterReplacement(self, s: str, K: int) -> int:
        ans = float('-inf')
        hm = defaultdict(int)
        mf = 0
        l = 0
        for k,v in enumerate(s):
            hm[v]+=1
            mf = max(mf,hm[v])
            
            is_valid = (k+1-l-mf<=K)
            
            if not is_valid:
                hm[s[l]]-=1
                l+=1
            ans = k+1-l
            
        return ans
        