class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        def wb(word,i,w):
            if i == len(word):
                self.ans.append(" ".join(w))
                return True
            for j in range(i,len(word)+1):
                if word[i:j] in wordDict:
                    w.append(word[i:j])
                    wb(word,j,w)
                    w.pop()
                
            return False
        wb(s,0,[])
        return self.ans
        