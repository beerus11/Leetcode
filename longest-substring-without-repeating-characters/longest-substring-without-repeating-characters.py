class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        ml = 0
        lp = 0
        for k,v in enumerate(s):
            if v in last_index:
                lp= max(lp,last_index[v]+1)
            last_index[v]=k
            ml= max(ml,k-lp+1)
        return ml
            
        
        