class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = defaultdict(int)
        s = set()
        for a,b in paths:
            if a in s:
                s.remove(a)
            outdegree[a]+=1
            s.add(b)
        for k,v in outdegree.items():
            if k in s:
                s.remove(k)
        return list(s)[0]
        