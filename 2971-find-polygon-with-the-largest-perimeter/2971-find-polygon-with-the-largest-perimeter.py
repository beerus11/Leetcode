class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = sum(nums)
        
        i = len(nums)-1
        
        while i >0:
            s-=nums[i]
            if s>nums[i]:
                return s+nums[i]
            i-=1
        return -1
            