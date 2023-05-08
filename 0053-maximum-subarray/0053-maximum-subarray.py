class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxs = 0
        mx_till_now = 0
        for i in nums:
            mx_till_now+=i
            if mx_till_now<0:
                mx_till_now=0
            mxs = max(mxs,mx_till_now)
        return max(nums) if mxs==0 else mxs
        