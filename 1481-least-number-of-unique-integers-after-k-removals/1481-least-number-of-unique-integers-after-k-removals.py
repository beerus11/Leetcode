class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hm = Counter(arr)
        freqs = sorted(hm.values())
        element_removed = 0
        for i,f in enumerate(freqs):
            element_removed+=f
            if element_removed>k:
                return len(freqs)-i    
        return 0