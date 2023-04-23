from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calander = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calander.bisect_right((start,end))
        
        if idx>0 and self.calander[idx-1][1]>start:
            return False
        if idx<len(self.calander) and self.calander[idx][0] < end:
            return False
        self.calander.add((start,end))
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)