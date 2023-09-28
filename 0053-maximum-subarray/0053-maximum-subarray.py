class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxs = 0
        max_till_now = 0
        for i in nums:
            max_till_now+=i
            if max_till_now<0:
                max_till_now = 0
            mxs = max(mxs,max_till_now)
        return mxs if mxs>0 else max(nums)
        