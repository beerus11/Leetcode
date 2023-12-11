class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        th = l/4
        pe,cnt = arr[0],1
        for i in range(1,len(arr)):
            if pe!=arr[i]:
                cnt=0
            cnt+=1
            pe=arr[i]
            if cnt>th:
                return pe
        return arr[0]
            
        