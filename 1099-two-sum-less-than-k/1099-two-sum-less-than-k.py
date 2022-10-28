class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i,j =0 , len(nums)-1
        mx = -1
        while i<j:
            s = nums[i]+nums[j]
            if s<k:
                mx = max(mx,s)
            if s<k:
                i+=1
            else:
                j-=1
        return mx
            
        