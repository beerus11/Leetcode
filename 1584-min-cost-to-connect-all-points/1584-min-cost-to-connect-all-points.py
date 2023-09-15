class UnionFind:
    def __init__(self,size):
        self.par = [0]*size
        self.rank = [0]*size
        
        for i in range(size):
            self.par[i]=i
            
    def find(self,node):
        if self.par[node]!=node:
            self.par[node]= self.find(self.par[node])
        return self.par[node]
    
    def join(self,node1,node2):
        grp1 = self.find(node1)
        grp2 = self.find(node2)
        
        if grp1==grp2:
            return False
        
        if self.rank[grp1]>self.rank[grp2]:
            self.par[grp2] = grp1
        elif self.rank[grp1]<self.rank[grp2]:
            self.par[grp1] = grp2
        else:
            self.par[grp1]=grp2
            self.rank[grp2]+=1
        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        
        for a in range(n):
            for b in range(a+1,n):
                w = abs(points[a][0] - points[b][0]) +abs(points[a][1] - points[b][1])
                edges.append((w,a,b))
        
        edges.sort()
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for w,n1,n2 in edges:
            if uf.join(n1,n2):
                mst_cost+=w
                edges_used+=1
                if edges_used == n-1:
                    break
        return mst_cost
            
        
        
            
            
        