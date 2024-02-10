from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.arr = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        idx = self.arr.bisect_right((start, end))
        if idx > 0 and self.arr[idx-1][1] > start:
            return False
        if idx < len(self.arr) and self.arr[idx][0] < end:
            return False
            
        self.arr.add((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)