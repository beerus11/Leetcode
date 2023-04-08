class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s[0]
        l = len(s)
        dp = [[False]*l for i in range(l)]
        
        mx,ans = 1,s[0]
        for i in range(l):
            dp[i][i] = True
            
        for i in range(l-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                mx=2
                ans=s[i:i+2]
                
        for j in range(2,l):
            for i in range(l-2):
                if i+j<l:
                    #print(i,j)
                    if dp[i+1][i+j-1] and s[i]==s[i+j]:
                        dp[i][i+j]=True
                        if j+1>mx:
                            mx = j+1
                            ans = s[i:i+j+1]
        return ans
                    
        