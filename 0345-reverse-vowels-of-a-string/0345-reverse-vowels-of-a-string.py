class Solution:
    def reverseVowels(self, s: str) -> str:
        vs = set(['a','e','i','o','u','A','E','I','O','U'])
        arr = list(s)
        vowels = []
        i = 0
        while i<len(arr):
            if arr[i] in vs:
                vowels.append(arr[i])
            i+=1
        vowels = vowels[::-1]
        i=0
        while i<len(s):
            if arr[i] in vs:
                arr[i]=vowels.pop(0)
            i+=1
        return "".join(arr)
        