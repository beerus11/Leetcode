class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        def check_palin(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        i,j = 0,len(s)-1
        while i < j:
            if s[i]!=s[j]:
                return check_palin(s,i,j-1) or check_palin(s,i+1,j)
            i+=1
            j-=1
        return True
        