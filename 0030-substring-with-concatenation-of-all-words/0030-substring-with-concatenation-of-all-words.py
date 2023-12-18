class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        k = len(words)
        n= l*k
        mp = Counter(words)
        
        def check(i):
            rem = mp.copy()
            used = 0
            for j in range(i,i+n,l):
                st = s[j:j+l]
                if rem[st]>0:
                    rem[st]-=1
                    used+=1
                else:
                    break
                    
            return used==k
        
        ans = []
        for i in range(len(s)-n+1):
            if check(i):
                ans.append(i)
        return ans
                
        