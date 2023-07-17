class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        arr = []
        ans = 0
        k = -inf
        
        for a,b in intervals:
            if a>=k:
                k=b
            else:
                ans+=1
        return ans
            
            
            
        