class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        ls,l = "",0
        for i in range(len(s)):
            for j in range(len(s)):
                hm[s[i:j+1]]+=1
                if hm[s[i:j+1]]>1:
                    l = max(l,len(s[i:j+1]))
        return l
        