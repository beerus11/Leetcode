class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(filter(lambda x:len(x)>0,s.strip().split(" ")[::-1])))
        