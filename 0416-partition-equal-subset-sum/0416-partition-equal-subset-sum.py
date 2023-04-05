class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        t = s/2
        self.dp = {}
        def ss(nums,sm,i):
            if (sm,i) in self.dp:
                return self.dp[(sm,i)]
            if i>=len(nums):
                self.dp[(sm,i)] = False
                return self.dp[(sm,i)]
            if sm == t:
                self.dp[(sm,i)] =  True
                return self.dp[(sm,i)]
            a = ss(nums,sm+nums[i],i+1)
            if a:
                self.dp[(sm,i)] = True
                return True
            self.dp[(sm,i)] = ss(nums,sm,i+1)
            return self.dp[(sm,i)]
        return ss(nums,0,0)