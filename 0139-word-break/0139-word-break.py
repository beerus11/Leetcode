class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        dp = {}
        def wb(i,s):
            if i in dp:
                return dp[i]
            if i==len(s):
                dp[i]= True
                return dp[i]
            for j in range(i+1,len(s)+1):
                #print(s[i:j],s[i:j] in wd)
                if s[i:j] in wd and wb(j,s):
                    dp[i]= True
                    return dp[i]
            dp[i] = False
            return dp[i]
                    
        return wb(0,s)