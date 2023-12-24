class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        @lru_cache(None)
        def dfs(i,j):
            if j == len(s2):
                return i

            ind = s1.find(s2[j],i+1)

            return float("inf") if ind == -1 else dfs(ind,j+1)

        l, res = float("inf"), ""
        for k,v in enumerate(s1):
            if v == s2[0]:
                j = dfs(k,1)
                if j-k < l:
                    l, res = j-k, s1[k:j+1]

        return res
        