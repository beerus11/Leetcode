class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.dp = {}
        def ts(i,t):
            if (i,t) in self.dp:
                return self.dp[(i,t)]
            elif t==target and i==len(nums):
                return 1
            elif i< len(nums):
                self.dp[(i,t)] = ts(i+1,t-nums[i])+ts(i+1,t+nums[i])
                return self.dp[(i,t)]
            return 0
        return ts(0,0)
                
        