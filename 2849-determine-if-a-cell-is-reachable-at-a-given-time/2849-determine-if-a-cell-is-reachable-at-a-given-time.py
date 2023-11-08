class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        w = abs(fx-sx)
        h = abs(fy-sy)      
        if w ==0 and h ==0 and t==1:
            return False
        return t>=max(h,w)
            
        