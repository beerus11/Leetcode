class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        ans = 1
        while self.arr and self.arr[-1][0] <= price:
            ans += self.arr.pop()[1]
            
        self.arr.append([price,ans])
        return ans
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)