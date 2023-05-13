class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        j,count=1,1
        while j<len(nums):
            ln = nums[j-1]
            while j<len(nums) and ln==nums[j]:
                nums[j]="_"
                j+=1
            if j<len(nums):
                count+=1
            j+=1
        i,j =0,0
        while j<len(nums) and i<len(nums):
            while j<len(nums) and nums[j]!="_":
                j+=1
            i=j+1
            while i<len(nums) and nums[i]=="_":
                i+=1
            if j<len(nums) and i<len(nums):
                nums[i],nums[j]=nums[j],nums[i]
            #i+=1
            
        return count
                
            
            
        