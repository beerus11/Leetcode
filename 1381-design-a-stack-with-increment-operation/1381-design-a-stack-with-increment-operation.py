class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.cap = maxSize
        

    def push(self, x: int) -> None:
        if len(self.st)< self.cap:
            self.st.append(x)
            
        
    def pop(self) -> int:
        if len(self.st)==0:
            return -1
        return self.st.pop()
        

    def increment(self, k: int, val: int) -> None:
        i =0
        while i<k and i<len(self.st):
            self.st[i]+=val
            i+=1
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)