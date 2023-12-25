class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.split(" ")
        if len(arr)<3:
            return False
        i = 2
        ans = []
        while i< len(arr):
            if arr[i-2]==first and arr[i-1]==second:
                ans.append(arr[i])
            i+=1
        return ans