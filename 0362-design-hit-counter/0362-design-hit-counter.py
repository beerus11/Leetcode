from collections import OrderedDict,defaultdict
class HitCounter:

    def __init__(self):
        self.d = OrderedDict()
        

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.d:
            self.d[timestamp] = []
        self.d[timestamp].append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        count =0
        for i in range(timestamp,timestamp-300,-1):
            if i in self.d:
                count+=len(self.d[i])
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)