import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1,10000))
        self.s = set(self.heap)
        heapq.heapify(self.heap)
        

    def popSmallest(self) -> int:
        if len(self.heap)==0:
            return 0
        no = heapq.heappop(self.heap)
        self.s.remove(no)
        return no
        

    def addBack(self, num: int) -> None:
        if num not in self.s:
            heapq.heappush(self.heap,num)
            self.s.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)