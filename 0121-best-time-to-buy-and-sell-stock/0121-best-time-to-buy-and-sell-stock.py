class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxP = float('-inf')
        mnP = float('inf')
        for p in prices:
            if p<mnP:
                mnP = p
            mxP=max(mxP,p-mnP)
        return mxP
            
        