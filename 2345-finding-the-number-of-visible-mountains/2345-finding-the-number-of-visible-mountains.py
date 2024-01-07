'''
 def visibleMountains(self, peaks: List[List[int]]) -> int:
        intervals = []
        for x, y in peaks:
            intervals.append((x - y, x + y))
        intervals.sort(key=lambda i: (i[0], -i[1]))

        ans = 0
        max_end = -inf
        for i in range(len(intervals)):
            start, end = intervals[i]
            next_is_same = (i < len(intervals) - 1 and intervals[i+1] == intervals[i])
            ans += (end > max_end and not next_is_same)
            max_end = max(end, max_end)
        return ans
'''
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        arr = [(a-b,a+b) for a,b in peaks]
        arr.sort(key=lambda i: (i[0], -i[1]))
        le =0
        count = 0
        for i in range(len(arr)):
            a,b = arr[i]
            next_is_same = False
            if i < len(arr) - 1 and arr[i+1] == arr[i]:
                next_is_same=True
            if le<b and not next_is_same:
                count+=1
            le = max(le,b)
        return count
        
        