class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        s = 0
        sum_till_now = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                sum_till_now+=1
                s +=sum_till_now
            else:
                sum_till_now = 0
        return s
                
                
        