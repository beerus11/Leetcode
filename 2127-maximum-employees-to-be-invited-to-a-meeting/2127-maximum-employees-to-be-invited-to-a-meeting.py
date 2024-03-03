class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.parents[x]:
            return self.find(self.parents[x])
        return x
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.size[xr] < self.size[yr]:
                x, y = y, x
            self.parents[yr] = xr
            self.size[xr] += self.size[yr]

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        tail_length = [1] * n
        inDegree = [0] * n
        
        for curr in range(n):
            inDegree[favorite[curr]] += 1
            
        queue = deque([c for c in range(n) if inDegree[c] == 0])
        
        while queue:
            curr = queue.popleft()
            fav = favorite[curr]
            tail_length[fav] = max(tail_length[fav], tail_length[curr] + 1)
            inDegree[fav] -= 1
            if inDegree[fav] == 0:
                queue.append(fav)
        print(inDegree,tail_length)
                
        # Building the Union Find of popular person
        uf = UnionFind(n)
        for i in range(n):
            if inDegree[i]:
                uf.union(i, favorite[i])
        print(uf.size)
        print(inDegree)

        join = 0
        res = 0
        for i in range(n):
            if not inDegree[i]:
                continue
            curr = uf.size[uf.find(i)]
            if curr == 2:
                fav = favorite[i]
                inDegree[fav] -= 1
                curr = tail_length[i] + tail_length[fav]
                join += curr
            else:
                res = max(res, curr)
        return max(res, join)