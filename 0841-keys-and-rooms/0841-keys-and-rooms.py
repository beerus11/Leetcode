class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(n):
            if n==None:
                return
            visited.add(n)
            for nei in rooms[n]:
                if nei not in visited :
                    dfs(nei)
        dfs(0)
        return len(visited)==n
            
        