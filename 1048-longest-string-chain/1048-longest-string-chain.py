class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        maxchain = 0
        for word in words:
            dp[word]=1
            for i in range(len(word)):
                w = word[:i]+word[i+1:]
                if w in dp:
                    dp[word]= max(dp[word],dp[w]+1)
                maxchain = max(maxchain,dp[word])
        return maxchain
        