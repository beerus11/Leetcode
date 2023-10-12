# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l,h = 1, mountain_arr.length()-2
        while l <h:
            mid = l+(h-l)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                l = mid+1
            else:
                h = mid
        peak = l
        def bsa(l,h):
            while l<=h:
                mid = l+(h-l)//2
                x = mountain_arr.get(mid)
                if x==target:
                    return mid
                elif x<target:
                    l = mid+1
                else:
                    h= mid-1
            return -1
        def bsd(l,h):
            while l<=h:
                mid = l+(h-l)//2
                x = mountain_arr.get(mid)
                if x==target:
                    return mid
                elif x>target:
                    l = mid+1
                else:
                    h= mid-1
            return -1
        
        ans = bsa(0,peak)
        if ans!=-1:
            return ans
        return bsd(peak+1, mountain_arr.length()-1)
      
        
            
        
        
        