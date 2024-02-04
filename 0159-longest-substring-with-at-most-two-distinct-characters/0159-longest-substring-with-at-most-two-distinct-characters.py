class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 1
        left =0
        hm = defaultdict(int)
        for k,v in enumerate(s):
            hm[v]+=1
            while len(hm)>2:
                hm[s[left]]-=1
                if hm[s[left]]==0:
                    del hm[s[left]]
                left+=1
            ans = max(ans,k-left+1)
        return ans
        