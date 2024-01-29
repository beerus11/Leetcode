class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        r = len(rooms)
        v = set()
        self.count = 0
        def dfs(node):
            if node==None or node in v:
                return
            self.count+=1
            v.add(node)
            for nei in rooms[node]:
                dfs(nei)
        dfs(0)
        return self.count == r