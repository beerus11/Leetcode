class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = []
        mxA =float('-inf')
        ls = 0
        for i in nums:
            ls+=i
            w.append(i)
            if len(w)>k:
                x = w.pop(0)
                ls-=x
            if len(w)==k:
                mxA = max(mxA,ls/k)
        return mxA
            
        