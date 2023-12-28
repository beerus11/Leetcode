class Solution:
    def reorderSpaces(self, text: str) -> str:
        arr = text.split()
        sc = text.count(" ")
        if len(arr)==1:
            return arr[0]+" "*sc
        div = " "*(sc//(len(arr)-1))
        end = " "*(sc%(len(arr)-1))
        return div.join(arr)+end