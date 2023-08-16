class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def ls(m,n,i):
            if i==len(strs) or (m==0 and n==0):
                return 0
            z = strs[i].count("0")
            o = len(strs[i])-z
            
            if z>m or o>n:
                return ls(m,n,i+1)
            a = ls(m,n,i+1)
            b = 1+ls(m-z,n-o,i+1)
            return max(a,b)
        return ls(m,n,0)
        