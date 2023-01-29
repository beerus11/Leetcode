class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        self.d = {}
        def dp(l,r):
            if (l,r) in self.d:
                return self.d[(l,r)]
            if l>r:
                return 0
            result = 0
            #print(l,r)
            for i in range(l,r+1):
                gain = nums[l-1]*nums[i]*nums[r+1]
                rem = dp(l,i-1)+dp(i+1,r)
                
                result = max(result,rem+gain)
            self.d[(l,r)]= result
            return self.d[(l,r)]
        return dp(1,len(nums)-2)