class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        i = 1
        while i<len(nums):
            j = 0
            while j <i:
                if nums[j]<nums[i] and lis[i]<lis[j]+1:
                    lis[i] = lis[j]+1
                j+=1
            i+=1
        return max(lis)
            
        