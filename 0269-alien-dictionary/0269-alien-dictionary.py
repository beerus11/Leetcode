from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:   
        indegree = {c : 0 for word in words for c in word}
        g = defaultdict(list)
        
        for i in range(len(words)-1):
            for a,b in list(zip(words[i],words[i+1])):
                if a!=b:
                    g[a].append(b)
                    indegree[b]+=1
                    break
            else:
                if len(words[i+1]) < len(words[i]): return ""
                
                    
        q = []
        for k,v in indegree.items():
            if v ==0:
                q.append(k)
                
        if len(q)==0 and len(indegree)==1:
            return words[0][0]

        order = []
        while q:
            n = q.pop(0)
            order.append(n)
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(indegree)> len(order):
            return ""
                    
        return "".join(order)
        
                    
        