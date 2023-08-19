from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x: (x[0],-x[1]))
        print(envelopes)
        
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp,nums[i])
                if idx==len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx]=nums[i]
            return len(dp)
        
        return lis([i[1] for i in envelopes])
        
        
        