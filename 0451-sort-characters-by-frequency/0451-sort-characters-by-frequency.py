class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s)
        arr = []
        for k,v in sorted(m.items(),key=lambda x:x[1],reverse=True):
            arr.append(v*k)
        return "".join(arr)
            
        