class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        arr = s.split(" ")
        if len(arr)!=len(p):
            print("k",len(arr),len(s))
            return False
        m1 = {}
        m2 = {}
        for k,v in enumerate(arr):
            x,y=v,p[k]
            #print(k,v,m1,m2)
            if x in m1 and y not in m2:
                return False
            if x in m1 and m1[x]!=y:
                #print("b")
                return False
            if x not in m1 and y in m2:
                return False
            if y in m2 and m2[y]!=x:
                return False
            m1[x]=y
            m2[y]=x
        return True
                