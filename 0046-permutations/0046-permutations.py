class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def p(i):
            if i==len(nums):
                self.ans.append(nums[:])
                return 
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                p(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        p(0)
        return self.ans