class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]
        self.ans = []
        def dfs(i,arr):
            if i>len(s):
                return
            if i==len(s):
                self.ans.append(arr[:])
                return

            for k in range(1,len(s)+1):
                x = s[i:i+k]
                if x==x[::-1]:
                    arr.append(x)
                    dfs(i+k,arr)
                    arr.pop()
        dfs(0,[])
        return self.ans
                    
                