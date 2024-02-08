class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        for i in range(len(s)):
            for j in range(i,len(s)):
                hm[s[i:j+1]]+=1
        mx=1
        ans = ""
        for k,v in hm.items():
            if v>1 and len(k)>mx:
                mx = len(k)
                ans = k
        if mx==1:
            return 0
        return len(ans)
                
        