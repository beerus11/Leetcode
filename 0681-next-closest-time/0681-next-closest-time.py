class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            arr = [d in allowed for a in divmod(cur,60) for d in divmod(a,10)]
            if all(arr):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))
            
        