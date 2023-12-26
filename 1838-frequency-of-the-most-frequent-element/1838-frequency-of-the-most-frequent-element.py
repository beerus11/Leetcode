class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0 
        ans = 1
        for right in range(len(nums)):
            curr+=nums[right]
            while ((right-left+1)*nums[right])-curr>k:
                curr-=nums[left]
                left+=1
            ans = max(ans,right-left+1)
        return ans
            
        