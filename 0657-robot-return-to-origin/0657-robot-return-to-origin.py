class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dirs = {'L':(-1,0),'R':(1,0),'U':(0,1),'D':(0,-1)}
        o = [0,0]
        for c in moves:
            i,j = dirs[c]
            o[0]+=i
            o[1]+=j
        return o==[0,0]