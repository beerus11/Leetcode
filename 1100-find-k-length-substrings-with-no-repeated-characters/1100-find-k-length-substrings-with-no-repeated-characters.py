class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        i=0
        j=k-1
        ans = 0
        hm = Counter(s[i:k])
        if len(hm)==k:
            ans=1
        while j<len(s):
            i+=1
            j+=1
            hm[s[i-1]]-=1
            if hm[s[i-1]]==0:
                del hm[s[i-1]]
            
            if j==len(s):
                return ans
            
            hm[s[j]]+=1    
            if len(hm)==k:
                ans+=1
        return ans
        