class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        print(citations)
        l = len(citations)
        i = 0
        while i<l and citations[l-i-1]>i:
            i+=1
        return i