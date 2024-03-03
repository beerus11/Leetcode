class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        
        g = defaultdict(list)
        for a,b in similarPairs:
            g[a].append(b)
            g[b].append(a)
        v = set()
        def dfs(src,dest):
            if src==dest:
                return True
            v.add(src)
            for nei in g[src]:
                if nei not in v and dfs(nei,dest):
                    return True  
            return False
            
        for i in range(len(sentence1)):
            v = set()
            if not dfs(sentence1[i],sentence2[i]):
                return False
            
        return True
        