class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.hm = {}
        for k,v in enumerate(order):
            self.hm[v]=k
        def compare(x,y):
            i = 0
            while i < min(len(x),len(y)) and x[i]==y[i]:
                if self.hm[x[i]]>self.hm[y[i]]:
                    return False
                i+=1
            print(i)
            if i<=len(x)-1 and i<=len(y)-1:
                return self.hm[x[i]]<self.hm[y[i]]
            print("h")
            if i<len(x) and len(x)>len(y):
                return False
            return True
        for i in range(1,len(words)):
            if not compare(words[i-1],words[i]):
                return False
        return True
        
        