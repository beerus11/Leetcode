class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        sum_till_now = 0
        for i in nums:
            sum_till_now+=i
            if sum_till_now<0:
                sum_till_now = 0
            ans = max(ans,sum_till_now)
        if ans ==0:
            return max(nums)
        return ans
            
        