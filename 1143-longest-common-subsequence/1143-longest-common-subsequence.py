class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        @lru_cache(None)
        def lcs(i,j):
            if i==len(t1) or j==len(t2):
                return 0
            if t1[i]==t2[j]:
                return 1+ lcs(i+1,j+1)
            return max(lcs(i+1,j),lcs(i,j+1))
        return lcs(0,0)