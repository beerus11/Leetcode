class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 
        def p(i=0):
            if i== n:
                ans.append(nums[:])
                return
            for j in range(i,n):
                nums[i],nums[j]=nums[j],nums[i]
                p(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        n = len(nums)
        ans = []
        p()
        return ans
        