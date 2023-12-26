from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:   
        g = defaultdict(list)
        indegree = {ch:0 for word in words for ch in word}
        for a,b in zip(words,words[1:]):
            if a==b:
                continue
            for i in range(len(words)-1):
                for a,b in list(zip(words[i],words[i+1])):
                    if a!=b:
                        g[a].append(b)
                        indegree[b]+=1
                        break
                else:
                    if len(words[i+1]) < len(words[i]): return ""
        print(g)    
        q = []
        for k,v in indegree.items():
            if v==0:
                q.append(k)
        ans = []
        while q:
            n = q.pop(0)
            ans.append(n)
            for nei in g[n]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(ans)<len(indegree):
            return ""
        return "".join(ans)
            
        
      
                    
        