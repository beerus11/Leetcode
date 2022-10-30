class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = float('inf')
        for p in prices:
            profit = p-minPrice
            maxP = max(profit,maxP)
            minPrice = min(minPrice,p)
            
        return maxP
        