class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for j in range(len(s)):
            ps_hm = defaultdict(int)
            ng_hm = defaultdict(int)
            left = j
            for i in range(j,len(s)):
                ch = s[i]
                if ch in ps_hm:
                    ps_hm[ch]+=1
                else:
                    ng_hm[ch]+=1
                    if ng_hm[ch]==k:
                        ps_hm[ch]=k
                        del ng_hm[ch]
                if len(ng_hm)==0:
                    ans = max(ans,i-left+1)
        return ans
                    
            
            