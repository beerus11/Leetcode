class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        i = 1
        while i <len(prices):
            if prices[i]>prices[i-1]:
                mxp += prices[i]-prices[i-1]
            i+=1
        return mxp
                
        