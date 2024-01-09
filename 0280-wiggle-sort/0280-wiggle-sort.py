class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=2:
            nums.sort()
            return
        nums.sort()
        for i in range(2,len(nums),2):
            nums[i],nums[i-1]= nums[i-1],nums[i]
            
        