class Solution:

    def __init__(self, w: List[int]):
        self.total_sum =0
        self.arr = []
        prefix_sum = 0
        for i in w:
            prefix_sum+=i
            self.arr.append(prefix_sum)
        self.total_sum = prefix_sum
            
    def pickIndex(self) -> int:
        t = self.total_sum * random.random()
        for a,b in enumerate(self.arr):
            if t<b:
                return a
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()