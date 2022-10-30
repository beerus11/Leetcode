class Solution:
    def racecar(self, target: int) -> int:
        q = [(0,0,1)]
        visited = set()
        while q:
            moves,pos,speed = q.pop(0)
            
            if pos == target:
                return moves
            
            if (pos,speed) in visited:
                continue
            else:
                visited.add((pos,speed))
                
            q.append((moves+1,pos+speed,speed*2))
            
            if (pos+speed>target and speed>0) or (pos+speed<target and speed<0):
                speed = -1 if speed>0 else 1
                q.append((moves+1,pos,speed))
        return -1
                
            