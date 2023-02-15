from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = defaultdict(int)
        for i in words:
            hm[i]+=1
        arr = sorted(hm.items(),key= lambda a:(-1*a[1],a[0]))
        return [i[0] for i in arr[:k]]
        