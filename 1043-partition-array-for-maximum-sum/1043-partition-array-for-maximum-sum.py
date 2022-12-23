class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.dp = {}
        def msa(nums,index):
            if index >= len(nums):
                return 0
            if index in self.dp:
                return self.dp[index]
            ans = -1*float('inf')
            maxInt = -1*float('inf')
            l = 0
            for i in range(index,min(index+k,len(nums))):
                l+=1
                maxInt = max(maxInt,nums[i])
                s = l*maxInt + msa(nums,i+1)
                ans = max(ans,s)
            self.dp[index]= ans
            return ans
        return msa(arr,0)