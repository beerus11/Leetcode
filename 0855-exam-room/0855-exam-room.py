from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.s = SortedList()
        self.n = n
        
    def seat(self) -> int:
        if len(self.s)==0:
            self.s.add(0)
            return 0
        
        diff = self.s[0]
        idx = 0
        for a,b in zip(self.s,self.s[1:]):
            x = (b-a)//2
            if x>diff:
                diff=x
                idx=a+x
        if (self.n-1)-self.s[-1]>diff:
            diff = self.n-1 - self.s[-1]
            idx= self.n-1
        self.s.add(idx)
        return idx
            
    def leave(self, p: int) -> None:
        self.s.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)