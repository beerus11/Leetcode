class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9+7
        arr.sort()
        dp = [1]*len(arr)
        hm = {v:k for k,v in enumerate(arr)}
        for k,v in enumerate(arr):
            for j in range(k):
                if v%arr[j]==0:
                    node = v//arr[j]
                    if node in hm:
                        dp[k]+=(dp[j]*dp[hm[node]])
                        dp[k]%=mod
        return sum(dp)%mod