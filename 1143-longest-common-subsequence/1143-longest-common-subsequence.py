class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = {}
        def lcs(s,t,i,j):
            if i == len(s) or j == len(t):
                return 0
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if s[i]==t[j]:
                self.dp[(i,j)] = 1+ lcs(s,t,i+1,j+1)
            else:
                a = lcs(s,t,i+1,j)
                b = lcs(s,t,i,j+1)
                self.dp[(i,j)] = max(a,b)
            return self.dp[(i,j)]
        return lcs(text1,text2,0,0)
        