class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        m2 = {}
        for k,v in enumerate(t):
            if s[k] in m and m[s[k]]!=v:
                return False
            m[s[k]]=v
            
            if v in m2 and m2[v]!=s[k]:
                return False
            m2[v]=s[k]
        return True