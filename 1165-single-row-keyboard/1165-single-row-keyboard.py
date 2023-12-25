class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        m = {}
        for i in range(len(keyboard)):
            m[keyboard[i]]=i
        ans = 0
        idx = 0
        i =0 
        while i <len(word):
            new_idx = m[word[i]]
            ans+=abs(new_idx-idx)
            idx = new_idx
            i+=1
        return ans
            
        