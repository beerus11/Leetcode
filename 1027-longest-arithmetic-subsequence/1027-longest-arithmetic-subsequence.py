class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for right in range(len(nums)):
            for left in range(right):
                d = nums[right]-nums[left]
                dp[(right,d)]=dp.get((left,d),1)+1
        return max(dp.values())
        