class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]
        def dfs(ans,arr,s):
            if len(s)==0:
                ans.append(arr[:])
                return
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    dfs(ans,arr+[s[:i]],s[i:])
        ans = []
        dfs(ans,[],s)
        return ans