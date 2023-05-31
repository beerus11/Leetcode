class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        mx = -1
        for right in range(len(nums)):
            k -= 1-nums[right]
            if k<0:
                k+=1-nums[l]
                l+=1
            mx = max(mx,right-l+1)
        return mx
        