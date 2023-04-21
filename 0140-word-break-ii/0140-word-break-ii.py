class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        def wb(word,arr,i):
            if i== len(word):
                self.ans.append(" ".join(arr))
                return
            for j in range(i,len(word)+1):
                if word[i:j] in wordDict:
                    arr.append(word[i:j])
                    wb(word,arr[:],j)
                    arr.pop()
        wb(s,[],0)
        return self.ans
        