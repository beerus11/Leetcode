class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        result = []
        def dfs(node):
            for i in range(k):
                nnode = node+str(i)
                if nnode not in visited:
                    visited.add(nnode)
                    dfs(nnode[1:])
                    result.append(str(i))
        dfs("0"*(n-1))
        result.extend(["0"]*(n-1))
        return "".join(result)
                
                
        