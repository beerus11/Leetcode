class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        answer = 1
        dp = {}
        max_till_now = 0
        for a in arr:
            max_till_now = dp.get(a-difference,0)
            dp[a]=max_till_now+1
            answer = max(answer,dp[a])
        return answer
            
        