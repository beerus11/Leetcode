class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,b=0,len(nums)-1
        while a<=b:
            m = (a+b)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                b=m-1
            else:
                a=m+1
        return -1
        