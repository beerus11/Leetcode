class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = sorted(Counter(arr).items(),key = lambda x:x[1])
        i =0
        while i<len(arr):
            a,b = arr[i]
            if b<=k:
                k-=b
                i+=1
            else:
                break
        return len(arr)-i