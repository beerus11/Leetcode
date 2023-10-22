class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        mx_score = -1
        i,j=k,k
        mn_no = float('inf')
        while i>0 or j<len(nums)-1:
            if i == 0 or (j < len(nums) - 1 and nums[j + 1] > nums[i - 1]):
                j+=1
            else:
                i-=1
            mn_no= min([mn_no,nums[i],nums[j]])
            mx_score = max(mx_score,mn_no*(j-i+1))
        return mx_score
            