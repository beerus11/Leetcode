class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        edges = [jug1Capacity,jug2Capacity,-jug1Capacity,-jug2Capacity]
        q = [0]
        total = 0
        seen = set()
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False
        while q:
            node = q.pop(0)
            for e in edges:
                x = node+e
                if x==targetCapacity:
                    return True
                if x not in seen and x>=0 and x<=jug1Capacity+jug2Capacity:
                    q.append(x)
                    seen.add(x)
        return False
                
        