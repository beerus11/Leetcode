class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        
        dp = [[False]*l for i in range(l)]
        
        for i in range(l):
            dp[i][i]=True
            
        mx,ans = 1,s[0]
        
        for i in range(1,l):
            if s[i]==s[i-1]:
                dp[i-1][i]=True
                mx = 2
                ans = s[i-1:i+1]
                
        for j in range(2,l):
            for i in range(l-2):
                if i+j < l:
                    if s[i]==s[i+j] and dp[i+1][i+j-1]:
                        dp[i][i+j]=True
                        if j+1>mx:
                            mx = j+1
                            ans = s[i:i+j+1]
        return ans