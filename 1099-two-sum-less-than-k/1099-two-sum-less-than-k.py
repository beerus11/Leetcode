class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        mxs = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<k:
                    mxs = max(mxs,nums[i]+nums[j])
        return mxs
        