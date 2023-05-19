class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        j= 0
        while z<len(nums) and j<len(nums):
            while z<len(nums) and nums[z]!=0:
                z+=1
            while j<len(nums) and (nums[j]==0 or z>j):
                j+=1
            if j<len(nums) and z<len(nums) and z<j:
                nums[z],nums[j] = nums[j],nums[z]
                z+=1
            