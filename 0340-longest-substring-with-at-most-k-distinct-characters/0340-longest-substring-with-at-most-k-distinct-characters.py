class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        q = []
        hm = defaultdict(int)
        mxL = 0
        p = 0
        for i in range(len(s)):
            hm[s[i]]+=1
            
            while len(hm)>k:
                hm[s[p]]-=1
                if hm[s[p]]==0:
                    del hm[s[p]]
                p+=1
                
            mxL = max(mxL,i-p+1)
        return mxL
            
        