class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        prev = 0
        for i in range(len(arr)):
            if arr[i] == " " or i==len(arr)-1:
                a,b = prev,i-1
                if i==len(arr)-1:
                    b = i
                while a<b:
                    arr[a],arr[b]=arr[b],arr[a]
                    a+=1
                    b-=1
                prev = i+1
        return "".join(arr)
                
            
        