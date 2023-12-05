class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tw = sum(weights)
        l, h = max(weights), tw+1
        def get_days(arr,k):
            count = 1
            i = 0
            wt = 0
            while i < len(arr):
                wt+=arr[i]
                if wt>k:
                    count+=1
                    wt = arr[i]
                i+=1
            return count
        while l<h:
            mid = l+(h-l)//2
            dys = get_days(weights,mid)
            if dys>days:
                l=mid+1
            else:
                h=mid
        return h
                
            
        