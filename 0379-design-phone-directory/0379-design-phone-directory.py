class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.arr = [True]*maxNumbers
        

    def get(self) -> int:
        index = -1
        for k,v in enumerate(self.arr):
            if v==True:
                index = k
                break
        self.arr[index] = False
        return index
        

    def check(self, number: int) -> bool:
        return self.arr[number]
        

    def release(self, number: int) -> None:
        self.arr[number] = True
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)