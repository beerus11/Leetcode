class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1,(l//2) + 1):
            if l%i==0:
                p = s[:i]*(l//i)
                if s == p:
                    return True
        return False
             
        