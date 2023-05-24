class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        ans = 0
        i = len(self.q)-1
        while i>=0 and self.q[i]>=t-3000:
            ans+=1
            i-=1
        return ans


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)