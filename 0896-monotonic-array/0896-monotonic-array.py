class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        a = all([nums[i]>=nums[i+1]for i in range(len(nums)-1)])
        b = all([nums[i]<=nums[i+1]for i in range(len(nums)-1)])
        
        return a or b
            
        