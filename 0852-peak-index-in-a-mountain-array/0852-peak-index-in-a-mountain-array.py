class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,h = 0,len(arr)-1
        while l<h:
            mid = l+(h-l)//2
            if arr[mid]<arr[mid+1]:
                l=mid+1
            else:
                h=mid
        return l