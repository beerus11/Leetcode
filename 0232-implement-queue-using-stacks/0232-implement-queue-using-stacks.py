class MyQueue:

    def __init__(self):
        self.st = []
        self.pt = -1
        

    def push(self, x: int) -> None:
        self.st.append(x)
        

    def pop(self) -> int:
        if self.pt+1 ==len(self.st):
            return -1
        x = self.st[self.pt+1]
        self.pt+=1
        return x
            

    def peek(self) -> int:
        return self.st[self.pt+1]
        

    def empty(self) -> bool:
        return self.pt+1 ==len(self.st)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()