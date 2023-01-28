class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.d = {}
        

    def insert(self, val: int) -> bool:
        #print("insert",self.arr,self.d)
        if val in self.d:
            return False
        self.arr.append(val)
        self.d[val]=len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        #print("remove",self.arr,self.d)
        ind = self.d[val]
        l = len(self.arr)-1
        self.arr[l],self.arr[ind]=self.arr[ind],self.arr[l]
        del self.d[val]
        if ind!=l:
            self.d[self.arr[ind]]=ind
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        x = int(random.random()*len(self.arr))
        #print(self.arr,self.d)
        return self.arr[x]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()