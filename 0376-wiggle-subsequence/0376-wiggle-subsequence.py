class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        prev_diff = nums[1]-nums[0]
        ans = 2 if prev_diff !=0 else 1
        for i in range(2,len(nums)):
            diff = nums[i]-nums[i-1]
            if (diff>0 and prev_diff<=0) or (diff<0 and prev_diff>=0):
                ans+=1
                prev_diff = diff
        return ans
        
            
        