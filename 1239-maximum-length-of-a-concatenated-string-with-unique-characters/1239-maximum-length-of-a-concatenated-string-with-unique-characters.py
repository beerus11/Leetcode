class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def ml(i,s):
            if i==len(arr):
                return 0
            t = set(arr[i])
            if len(t-s)<len(t) or len(set(arr[i]))<len(arr[i]):
                return ml(i+1,s)
            else:
                return max(len(arr[i])+ml(i+1,s.union(t)),ml(i+1,s))
        return ml(0,set())
        