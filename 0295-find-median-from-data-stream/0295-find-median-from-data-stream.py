import heapq
class MedianFinder:

    def __init__(self):
        self.lo = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo,-1*num)
        
        heapq.heappush(self.high,-1*heapq.heappop(self.lo))
        
        if len(self.lo)<len(self.high):
            heapq.heappush(self.lo,-1*heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.lo)>len(self.high):
            return -1*self.lo[0]
        return (-1*self.lo[0]+self.high[0])*0.5
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()