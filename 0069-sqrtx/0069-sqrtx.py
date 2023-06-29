class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        start,end = 1,x
        while start <=end:
            mid = start+(end-start)//2
            if mid**2 == x:
                return mid
            elif mid**2>x:
                end= mid-1
            else:
                start = mid+1
        if start**2 >x:
            return start-1
        return start
        