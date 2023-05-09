class Solution:
    def racecar(self, target: int) -> int:
        q = [(0,0,1)]
        visited = set()
        
        while q:
            m,p,s = q.pop(0)
            if p==target:
                return m
            if (p,s) in visited:
                continue
            else:
                visited.add((p,s))
                q.append((m+1,p+s,s*2))
            
                if (p+s>target and s>0) or (p+s<target and s<0):
                    s = -1 if s>0 else 1
                    q.append((m+1,p,s))
                    
                
        