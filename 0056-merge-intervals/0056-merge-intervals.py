class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key= lambda a: a[0])
        print(intervals)
        arr = [intervals[0]]
        
        for i in range(len(intervals)):
            a,b = intervals[i]
            if a>arr[-1][1]:
                arr.append([a,b])
            else:
                x,y = arr.pop()
                arr.append([x,max(b,y)])
        return arr
        
        