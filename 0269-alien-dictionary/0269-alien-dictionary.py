from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        g = defaultdict(list)
        
        indegree = {c:0 for word in words for c in word}
        for fw,sw in zip(words,words[1:]):
            for a,b in zip(fw,sw):
                if a!=b:
                    if b not in g[a]:
                        g[a].append(b)
                        indegree[b]+=1
                    break
            else:
                if len(sw)<len(fw): return ""
        output = []
        q = [a for a in indegree if indegree[a]==0]
        
        while q:
            c = q.pop(0)
            output.append(c)
            for i in g[c]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(output)<len(indegree):
            return ""
        return "".join(output)
                    
                
            
        