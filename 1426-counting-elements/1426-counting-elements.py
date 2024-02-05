class Solution:
    def countElements(self, arr: List[int]) -> int:
        hm = Counter(arr)
        count=0
        for i in arr:
            if i+1 in hm:
                count+=1

        return count
        