import random
class RandomizedSet:

    def __init__(self):
        self.hm = defaultdict()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.hm[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        
        key = self.hm[val]      
        
        self.arr[key],self.arr[-1]=self.arr[-1],self.arr[key]
        self.hm[self.arr[key]] =key
        self.arr.pop()
        del self.hm[val]

        return True
        
    def getRandom(self) -> int:
        key = random.randint(0,len(self.arr)-1)
        val = self.arr[key]
        last_val = self.arr[-1]
        
        self.hm[val] = len(self.arr)-1
        self.hm[last_val]= key
        self.arr[-1],self.arr[key] = self.arr[key],self.arr[-1]
        return last_val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()