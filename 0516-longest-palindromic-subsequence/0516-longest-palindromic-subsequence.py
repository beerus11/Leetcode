class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def lps(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return 2+lps(i+1,j-1)
            a = lps(i+1,j)
            b = lps(i,j-1)
            
            return max(a,b)
        return lps(0,len(s)-1)
            
            
        