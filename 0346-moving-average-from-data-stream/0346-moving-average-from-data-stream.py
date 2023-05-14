class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size
        self.s = 0
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.s+=val
        if len(self.arr)>self.size:
            self.s -=self.arr.pop(0)
        return self.s/len(self.arr)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)