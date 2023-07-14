class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = set(['a','e','i','o','u'])
        mvow,vow = 0,0
        sw = []
        for i in range(len(s)):
            sw.append(s[i])
            if s[i] in vs:
                vow +=1
            if len(sw)>k:
                e = sw.pop(0)
                if e in vs:
                    vow-=1
            mvow = max(mvow,vow)
        return mvow
            
        