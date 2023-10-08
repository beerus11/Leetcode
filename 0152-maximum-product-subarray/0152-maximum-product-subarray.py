class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = max_so_far
        
        for i in nums[1::]:
            t = max(i,max_so_far*i,min_so_far*i)
            min_so_far = min(i,max_so_far*i,min_so_far*i)
            
            max_so_far = t
            ans = max(ans,max_so_far)

        return ans 
                
        