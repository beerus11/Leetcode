class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par = list(range(26))
        def find(x):
            if x!=par[x]:
                x = find(par[x])
            return x
        def union(x,y):
            a,b = find(x),find(y)
            par[a]=b
        av = ord('a')
        for e in equations:
            if e[1]=="=":
                x,y = ord(e[0])-av,ord(e[3])-av
                union(x,y)
        for e in equations:
            if e[1]=="!":
                x,y = ord(e[0])-av,ord(e[3])-av
                if find(x) == find(y):
                    return False    
        return True