class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)
        for i in range(len(s)):
            hm[s[i]]+=1
        es, mo = 0,0
        for k,v in hm.items():
            if v%2==0:
                es+=v
            elif v>mo:
                es= es+ max(0,(mo-1))
                mo=v
            else:
                es+=(v-1)
        return es+mo
                    
        