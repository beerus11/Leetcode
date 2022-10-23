from collections import defaultdict
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def index(ch):
            return ord(ch)-ord('a')
        self.g = defaultdict(list)
        
        for e in equations:
            if e[1] == "=":
                a,b = index(e[0]),index(e[-1])
                self.g[a].append(b)
                self.g[b].append(a)
            
        color = [-1]*26
        
        def dfs(node,c):
            if color[node]==-1:
                color[node]=c
                for nei in self.g[node]:
                    dfs(nei,c)
                    
        for i in range(26):
            if color[i]==-1:
                dfs(i,i)
                
        for e in equations:
            if e[1]=="!":
                a,b = index(e[0]),index(e[-1])
                if color[a]==color[b]:
                    return False
        return True
                