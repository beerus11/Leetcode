class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False
        edges = [jug1Capacity,jug2Capacity,-jug2Capacity,-jug1Capacity]
        
        s = set()
        q = [0]
        while q:
            n = q.pop(0)
            for e in edges:
                x = n+e
                if x==targetCapacity:
                    return True
                if x not in s and x>=0 and x<=jug1Capacity+jug2Capacity:
                    q.append(x)
                    s.add(x)
        return False
                