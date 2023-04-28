class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        s = set() 
        for a,b in edges:
            degree[a]+=1
            degree[b]+=1
            s.add(a)
            s.add(b)
        l = len(s)
        for k,v in degree.items():
            if v==l-1:
                return k
        return -1