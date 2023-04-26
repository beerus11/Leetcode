import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.d = {}
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.arr.append(val)
        self.d[val]=len(self.arr)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        idx = self.d[val]
        l = len(self.arr)-1
        self.arr[idx],self.arr[-1] = self.arr[-1],self.arr[idx]
        self.arr.pop()
        if idx!=l:
            self.d[self.arr[idx]]=idx
        del self.d[val]
        return True
        

    def getRandom(self) -> int:
        a = int(random.random()*(len(self.arr)))
        return self.arr[a]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()