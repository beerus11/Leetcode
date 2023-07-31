class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def cost(i,j):
            if i <0 :
                dc = 0
                for p in range(j+1):
                    dc+=ord(s2[p])
                return dc
            if j <0 :
                dc = 0
                for p in range(i+1):
                    dc+=ord(s1[p])
                return dc
            if s1[i]==s2[j]:
                return cost(i-1,j-1)
            a = ord(s1[i])+cost(i-1,j)
            b = ord(s2[j])+cost(i,j-1)
            c = ord(s1[i])+ord(s2[j])+cost(i-1,j-1)
            return min([a,b,c])
        return cost(len(s1)-1,len(s2)-1)