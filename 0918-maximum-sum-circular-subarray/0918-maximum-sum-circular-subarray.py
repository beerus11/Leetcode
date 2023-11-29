class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmx,cmn=0,0
        mxs,mns = nums[0],nums[0]
        total_sum = 0
        for i in nums:
            cmx = max(cmx,0)+i
            mxs = max(mxs,cmx)
            
            cmn = min(cmn,0)+i
            mns = min(mns,cmn)
            
            total_sum+=i
            
        if total_sum==mns:
            return mxs
        return max(mxs,total_sum-mns)
            
        