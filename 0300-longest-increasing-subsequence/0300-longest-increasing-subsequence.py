class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and lis[i]<lis[j]+1:
                    lis[i] = lis[j]+1
        return max(lis)