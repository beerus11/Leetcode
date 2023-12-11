class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        big_no = 2147483647
        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    q.append((i,j,0))
        while q:
            i,j,d = q.pop(0)      
            for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
                x,y = a+i,b+j
                if x<0 or y<0 or x>len(rooms)-1 or y>len(rooms[0])-1:
                    continue
                if rooms[x][y]!=big_no:
                    continue
                q.append((x,y,d+1))
                rooms[x][y]= d+1
                    