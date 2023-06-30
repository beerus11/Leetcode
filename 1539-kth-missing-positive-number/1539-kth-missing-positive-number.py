class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,h=0,len(arr)
        while l<h:
            mid=l+(h-l)//2
            if arr[mid]-mid>k:
                h=mid
            else:
                l=mid+1
        return l+k
        