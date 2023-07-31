class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        @lru_cache(None)
        def us(i,j):
            if i==m or n==j:
                return int(j==len(t))
            ans = 0
            if s[i] == t[j]:
                ans = us(i+1,j+1)
            ans += us(i+1,j)
            return ans
        return us(0,0)