class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        @lru_cache
        def wb(i,s):
            if i==len(s):
                return True
            for j in range(i+1,len(s)+1):
                #print(s[i:j],s[i:j] in wd)
                if s[i:j] in wd and wb(j,s):
                    return True
            return False
                    
        return wb(0,s)