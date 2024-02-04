class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, K: int) -> int:
        ans = 0
        left =0
        hm = defaultdict(int)
        for k,v in enumerate(s):
            hm[v]+=1
            while len(hm)>K:
                hm[s[left]]-=1
                if hm[s[left]]==0:
                    del hm[s[left]]
                left+=1
            ans = max(ans,k-left+1)
        return ans
        