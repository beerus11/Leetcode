from collections import defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        g = defaultdict(list)
        for i in range(len(friends)):
            g[i].extend(friends[i])
            
        visited = set()
        wv = []
        ans = []
        
        q = [(id,0)]
        visited.add(id)
        while q:
            node,l = q.pop(0)
            if l==level:
                wv.append(watchedVideos[node])
                continue
            for nei in g[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei,l+1))
        
        
        wv = [j for i in wv for j in i]
        #print(wv)
        m = defaultdict(int)
        
        for i,j in enumerate(wv):
            m[j]+=1
            
        arr = sorted(m.items(),key= lambda x: (x[1],x[0]))
        return [i[0] for i in arr]
        
        