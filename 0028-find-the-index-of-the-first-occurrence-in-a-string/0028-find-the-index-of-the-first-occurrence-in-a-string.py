class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j=0,0
        while i<len(haystack):
            j=0
            s = i
            while i<len(haystack) and j <len(needle) and needle[j]==haystack[i]:
                print(s)
                j+=1
                i+=1
            if j==len(needle):
                return s
            else:
                i=s
            i+=1
        return -1
        