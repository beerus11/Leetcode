class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i <len(nums):
            if nums[i]==val:
                nums[i]=-1
            i+=1
        i,j=0,0
        while i < len(nums) and j <len(nums):
            while i < len(nums) and nums[i]!=-1:
                i+=1
            while j <len(nums) and nums[j]==-1:
                j+=1
            if i < len(nums) and j <len(nums) and i<j:
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        count = 0
        for i in nums:
            if i==-1:
                break
            count+=1
        return count