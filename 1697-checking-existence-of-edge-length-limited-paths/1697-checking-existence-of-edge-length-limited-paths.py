        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = list(range(n))
        def find(node):
            if parents[node]!=node:
                parents[node]=find(parents[node])
            return parents[node]
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            if r1!=r2:
                parents[r2]=r1
        edgeList.sort(key = lambda x: x[2])   
        
        q = [(l,u,v,i) for i,(u,v,l) in enumerate(queries)]
        q.sort()
        
        m = len(queries)
        ans = [False]*m
        edge_size = len(edgeList)
        edge_index = 0
        
        for q_limit,u,v,i in q:
            while edge_index<edge_size and edgeList[edge_index][2]<q_limit:
                union(edgeList[edge_index][0],edgeList[edge_index][1])
                edge_index+=1
            ans[i]=find(u)==find(v)
        
        return ans
        
        