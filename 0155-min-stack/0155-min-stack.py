class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minn = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minn))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack and self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack and self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()