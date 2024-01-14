class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = 0
        st = 0
        m = defaultdict(int)
        mf  = 0 
        for i in range(len(s)):
            m[s[i]]+=1
            mf = max(mf,m[s[i]])
            
            is_valid = (i+1-st-mf<=k)
            if not is_valid:
                m[s[st]]-=1
                st+=1
            
            ls = i+1-st
        return ls
        