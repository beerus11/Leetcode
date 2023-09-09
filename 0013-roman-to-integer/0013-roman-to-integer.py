class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        i =0
        ans = 0
        while i<len(s)-1:
            if s[i:i+2] in m:
                ans+=m[s[i:i+2]]
                i+=1
            else:
                ans+=m[s[i]]
            i+=1
        if i<len(s):
            ans+=m[s[i]]
        return ans
                
            
            