class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = defaultdict(int)
        ans = set()
        for i in range(len(s)-9):
            a = s[i:i+10]
            hm[a]+=1
            if hm[a]>1:
                ans.add(a)
        return list(ans)
            
            
        