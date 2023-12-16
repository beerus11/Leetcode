class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        ml = 1
        hm = defaultdict(int)
        last = 0
        for k,v in enumerate(s):
            if v in hm:
                last = max(last,hm[v]+1)
                del hm[v]
            hm[v]=k
            ml = max(ml,k-last+1)
        return ml
            
        