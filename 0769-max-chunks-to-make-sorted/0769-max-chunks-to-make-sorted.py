class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = set()
        ans = 0
        for i in range(len(arr)):
            if i in s:
                s.remove(i)
            else:
                s.add(i)
                
            if arr[i] in s:
                s.remove(arr[i])
            else:
                s.add(arr[i])
            if len(s)==0:
                ans+=1
        return ans
            
            