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
        
        