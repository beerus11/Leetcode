class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i,j=0,len(letters)-1
        while i<=j:
            mid = (i+j)//2
            if letters[mid]<=target:
                i = mid+1
            else:
                j = mid-1
        if i == len(letters):
            return letters[0]
        else:
            return letters[i]
        