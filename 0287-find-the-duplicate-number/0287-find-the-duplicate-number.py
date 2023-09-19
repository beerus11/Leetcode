class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for k,v in enumerate(nums):
            if k==0:
                continue
            if nums[k-1]==nums[k]:
                print(k)
                return v
        return -1
        