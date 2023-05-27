class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(filter(lambda x:len(x)>0,s.strip().split(" ")[::-1]))
        return " ".join(arr)
        