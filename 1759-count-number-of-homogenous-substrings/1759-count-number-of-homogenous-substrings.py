class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        mod = 10**9 +7
        st = 0
        for i in range(len(s)):
            if i==0 or s[i]==s[i-1]:
                st+=1
            else:
                st =1
            ans +=st
            ans%=mod
        return ans
        