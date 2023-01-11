class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        i = 0
        arr = []
        while i < l:
            a,b = intervals[i]
            if len(arr)==0 or arr[-1][1]< a:
                arr.append(intervals[i])
            else:
                x,y = arr.pop()
                arr.append([x,max(b,y)])
            i+=1
        return arr
        
        