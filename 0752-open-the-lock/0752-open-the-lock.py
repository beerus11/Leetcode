class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = [('0000',0)]
        dl = set(deadends)
        seen = set()
        while q:
            n,c = q.pop(0)
            if n in dl:
                continue
            if n==target:
                return c
            for i in range(4):
                s = int(n[i])
                for j in [-1,1]:
                    no = n[:i]+str((s+j)%10)+n[i+1:]
                    if no not in seen:
                        seen.add(no)
                        q.append((no,c+1))
        return -1
                
                
        