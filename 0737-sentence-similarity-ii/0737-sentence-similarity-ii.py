class DSU:
    def __init__(self,l):
        self.par = {}
        self.rank = {}
    def add_word(self,w):
        if w not in self.par:
            self.par[w]=w
            self.rank[w]=0
            
    def is_present(self,w):
        return w in self.par
        
    def union(self,a,b):
        a_par = self.find(a)
        b_par = self.find(b)
        if a_par==b_par:
            return
        elif self.rank[a_par] < self.rank[b_par]:
            self.par[a_par]=b_par
        elif self.rank[a_par] > self.rank[b_par]:
            self.par[b_par]=a_par
        else:
            self.par[b_par]=a_par
            self.rank[a_par]+=1
    def find(self,a):
        if self.par[a]!=a:
            return self.find(self.par[a])
        return self.par[a]
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        dsu = DSU(len)
        for a,b in similarPairs:
            dsu.add_word(a)
            dsu.add_word(b)
            dsu.union(a,b)
            
        for i in range(len(sentence1)):
            if sentence1[i]==sentence2[i]:
                continue
            if dsu.is_present(sentence1[i]) and dsu.is_present(sentence2[i]) and dsu.find(sentence1[i]) == dsu.find(sentence2[i]):
                continue
            return False
        return True
        
        