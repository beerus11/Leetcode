class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        while l<=h:
            mid = l+(h-l)//2
            if nums[mid]>nums[-1]:
                l=mid+1
            else:
                h=mid-1
        low = l
        def bs(l,r,t):
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid]==t:
                    return mid
                elif nums[mid]>t:
                    r = mid-1
                else:
                    l=mid+1
            return -1
        ans = bs(0,low-1,target)
        if ans!=-1:
            return ans
        return bs(low,len(nums)-1,target)