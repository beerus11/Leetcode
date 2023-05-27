from collections import OrderedDict
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        hm= OrderedDict()
        ans = []
        lc = -1
        for c in chars:
            if lc!=-1 and lc!=c:
                ans.append(lc)
                v = hm[lc]
                if v!=1:
                    ans.extend(list(str(v)))
                del hm[lc]
            if c not in hm:
                hm[c]=1
            else:
                hm[c]+=1
            lc = c
        ans.append(lc)
        v = hm[lc]
        if v!=1:
            ans.extend(list(str(v)))

        hm = None
        i =0
        while i<len(ans):
            chars[i]=ans[i]
            i+=1
        return len(ans)
            
            
            
        
        