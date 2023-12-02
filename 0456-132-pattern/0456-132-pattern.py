class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        lme,rge = [nums[0]],[]
        for i in range(1,len(nums)):
            lme.append(min(lme[-1],nums[i]))
            
        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= lme[j]:
                continue
            while k < len(nums) and nums[k] <= lme[j]:
                k += 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False
        