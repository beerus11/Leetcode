class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs[0])==0:
            return ""
        i=0
        ans = []
        while i < len(strs[0]):
            for j in range(1,len(strs)):
                if i>= len(strs[j-1]) or i>= len(strs[j]) or strs[j-1][i] != strs[j][i] :
                    print("h")
                    return "".join(ans)
            print(i)    
            ans.append(strs[0][i])
            #print(ans)
            i+=1
        return "".join(ans) 

