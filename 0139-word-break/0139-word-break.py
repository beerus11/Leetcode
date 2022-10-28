class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp ={}
        def wb(word,i):
            if i in self.dp:
                return self.dp[i]
            if i==len(word):
                self.dp[i] = True
                return self.dp[i]
            for j in range(i,len(word)+1):
                if word[i:j] in wordDict and wb(word,j):
                    self.dp[i]=True
                    return self.dp[i]
            self.dp[i]=False
            return self.dp[i]
        return wb(s,0)