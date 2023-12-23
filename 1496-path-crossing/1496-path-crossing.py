class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y= 0,0
        v = set()
        v.add((0,0))
        for d in path:
            if d == "E":
                x = x+1
            elif d =="W":
                x = x-1
            elif d == "N":
                y = y+1
            elif d == "S":
                y = y-1
            if (x,y) in v:
                return True
            v.add((x,y))
        return False
            
        