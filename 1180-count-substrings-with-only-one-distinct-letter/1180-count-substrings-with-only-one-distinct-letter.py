class Solution:
    def countLetters(self, s: str) -> int:
        count = 0
        left = 0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                n = i-left
                count += n*(n+1)//2
                left = i
        if left<len(s):
            n = len(s)-left
            count += n*(n+1)//2
            
        return count
        