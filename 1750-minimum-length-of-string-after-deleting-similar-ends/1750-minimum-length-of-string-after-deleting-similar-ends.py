class Solution:
    def minimumLength(self, s: str) -> int:
        i,j = 0, len(s)-1
        while i <j and s[i]==s[j]:
            ch = s[i]
            while i+1<j and s[i+1]==ch:
                i+=1
            while j-1>i and s[j-1]==ch:
                j-=1
            i+=1
            j-=1
        return j-i+1
                