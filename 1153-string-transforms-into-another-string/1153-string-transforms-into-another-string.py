class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1)!=len(str2):
            return False
        if str1==str2:
            return True
        hm = {}
        s = set()
        for a,b in zip(str1,str2):
            if a in hm and hm[a]!=b:
                print(hm,hm[a],a,b)
                return False
            hm[a]=b
            s.add(b)
        if len(s)<26:
            return True
        return False