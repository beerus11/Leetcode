class DSU:
    def __init__(self):
        self.parent = list(range(26))
        
    def find(self,x):
        if x!=self.parent[x]:
            return self.find(self.parent[x])
        return x
        
    def union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if x==y:
            return False
        self.parent[x]=y
        return True
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        for eq in equations:
            if eq.find("!=")==-1:
                a = ord(eq[0])-97
                b = ord(eq[-1])-97
                if a!=b:
                    dsu.union(a,b)
        for eq in equations:
            if eq.find("!=")!=-1:
                a = ord(eq[0])-97
                b = ord(eq[-1])-97
                if a==b:
                    return False
                
                para = dsu.find(a)
                parb = dsu.find(b)
                if para==parb:
                    return False
        return True
                    
                
        