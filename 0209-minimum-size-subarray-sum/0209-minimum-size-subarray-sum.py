class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,s = 0,0
        curr_sum = 0
        mL = float('inf')
        while i <len(nums):
            curr_sum +=nums[i]
            while curr_sum>=target:
                mL = min(mL,i-s+1)
                curr_sum-=nums[s]
                s+=1
            #print(curr_sum,s)
            i+=1
        return 0 if mL==float('inf') else mL
            
        