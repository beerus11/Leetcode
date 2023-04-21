class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp = {}
        def wb(w,i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if len(w)==0:
                self.dp[(i,j)] = True
                return self.dp[(i,j)]
            if w[i:j] in wordDict:
                self.dp[(i,j)] = True
                return self.dp[(i,j)]
            for k in range(i,j):
                if w[i:k+1] in wordDict and wb(w,k+1,j):
                    self.dp[(i,j)] = True
                    return self.dp[(i,j)]
            self.dp[(i,j)] = False
            return self.dp[(i,j)]
        return wb(s,0,len(s))
                
        