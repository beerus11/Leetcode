class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        i,j=0,len(nums)-1
        while i<len(nums) and nums[i]==arr[i]:
            i+=1
        if i==len(nums):
            return 0
        while nums[j]==arr[j] and j>=0:
            j-=1
        if j==0:
            return 0
        if j<i:
            return 0
        return j-i+1