class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                self.two_sum(nums,i)
        return self.res
                
            
    def two_sum(self,nums,i):
        lo,high=i+1,len(nums)-1
        while lo<high:
            s = nums[lo]+nums[high]+nums[i]
            if s<0:
                lo+=1
            elif s>0:
                high-=1
            else:
                self.res.append([nums[i],nums[lo],nums[high]])
                lo+=1
                high-=1
                while lo<high and nums[lo]==nums[lo-1]:
                    lo+=1
            
        