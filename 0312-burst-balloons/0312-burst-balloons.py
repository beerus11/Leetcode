class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        
        print(nums)
        
        @lru_cache(None)
        def mc(l,r):
            if r>r:
                return 0
            mx = 0
            for i in range(l,r+1):
                a = nums[l-1]*nums[i]*nums[r+1]
                x = mc(l,i-1)+mc(i+1,r)
                mx = max(mx,a+x)
            return mx
        return mc(1,len(nums)-2)