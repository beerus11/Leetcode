class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i =1
        count =0
        prev = nums[0]
        while i <len(nums):
            if nums[i-1]==nums[i]:
                prev = nums[i]
                count+=1
            elif prev == nums[i]:
                count+=1
            else:
                count=0
            if count>=2: 
                nums[i]="_"
            i+=1
        i,j=0,0
        while j < len(nums):
            while i < len(nums) and nums[i]!="_":
                i+=1
            j =i
            while j < len(nums) and nums[j]=="_":
                j+=1
            if i<len(nums) and j<len(nums):
                nums[i],nums[j]=nums[j],nums[i]
        return i
            
        