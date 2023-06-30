class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l,h=0,len(nums)-1
        while l<=h:
            mid = l +(h-l)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>=target:
                h=mid-1
        if l>len(nums)-1 or nums[l]!=target:
            return [-1,-1]
        ans=[l]
        l,h=0,len(nums)-1
        while l<=h:
            mid = l +(h-l)//2
            print(mid,l,h)
            if nums[mid]>target:
                h=mid-1
            elif nums[mid]<=target:
                l=mid+1
        ans.append(h)
        return ans
                
            
        