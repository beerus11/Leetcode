class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.d = {}
        l = len(edges)
        g = defaultdict(list)
        for a,b in enumerate(edges):
            if b!=-1:
                g[a].append(b)
            
        def dfs(n,d):
            if n==None:
                return
            self.d[n]=d
            for nei in g[n]:
                if (nei not in self.d) or d+1< self.d[nei]:
                    dfs(nei,d+1)
        d1,d2 = {},{}
        dfs(node1,0)
        d1=self.d
        self.d = {}
        dfs(node2,0)
        d2=self.d
        
        arr = []
        for k,v in enumerate(edges):
            if k in d1 and k in d2:
                arr.append((max(d1[k],d2[k]),k))
        arr = sorted(arr,key= lambda x:x[0])
        if len(arr)==0:
            return -1
        print(arr)
        return arr[0][1]
        