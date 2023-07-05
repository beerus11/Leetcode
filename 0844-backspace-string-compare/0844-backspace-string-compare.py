class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a,b =[],[]
        for c in s:
            if c!="#":
                a.append(c)
            elif len(a)>0:
                a.pop()
        for c in t:
            if c!="#":
                b.append(c)
            elif len(b)>0:
                b.pop()
        return a==b