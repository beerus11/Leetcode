class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for h, i, j, k in itertools.permutations(arr):
            hour = h*10 + i
            mn = j*10 + k
            if hour<24 and mn<60:
                max_time = max(max_time,hour*60+mn)
                
        if max_time ==-1:
            return ""
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
                
            
        