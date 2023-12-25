class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==1 and s[0]!="0":
            return 1 
        if s[0]=="0":
            return 0
        @lru_cache(None)
        def no(st,i):
            if i==len(st):
                return 1
            if i==len(st)-1 and st[i]=="0":
                return 0
            if i==len(st)-1:
                return 1
            a = 0
            if s[i]!="0":
                a += no(st,i+1)
            if s[i]!="0" and int(st[i:i+2])<=26:
                a+=no(st,i+2)
            return a
                
        return no(s,0)
        