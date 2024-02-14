class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_far = 0
        cur_end = 0
        ans = 0 
        for i in range(len(nums)-1):
            cur_far = max(cur_far,nums[i]+i)
            if i== cur_end:
                ans +=1
                cur_end = cur_far
        return ans
            
        