class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bs(arr):
            l, h = 0, len(arr)-1
            while l <h:
                mid = l + (h-l)//2
                #print(mid)
                if arr[mid]>=0:
                    l=mid+1
                else:
                    h=mid
            if arr[l]>=0:
                return len(arr)
            return l
        count = 0
        for row in grid:
            #print(bs(row))
            count += (len(row) - bs(row))
        return count
        