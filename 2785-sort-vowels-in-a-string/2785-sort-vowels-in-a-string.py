class Solution:
    def sortVowels(self, s: str) -> str:
        arr = list(s)
        vowels = []
        s = set(['a','e','i','o','u','A','E','I','O','U'])
        for k,v in enumerate(arr):
            if v in s:
                arr[k]=-1
                vowels.append(v)
        vowels.sort()
        for i in range(len(arr)):
            if arr[i]==-1:
                arr[i]=str(vowels.pop(0))
            else:
                arr[i]=str(arr[i])
        return "".join(arr)
        