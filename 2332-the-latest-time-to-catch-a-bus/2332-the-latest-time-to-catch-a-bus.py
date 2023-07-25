'''
 passengers.sort()
        cur = 0

        for time in sorted(buses):
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur - 1]

        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best
'''
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        p = 0
        for b in sorted(buses):
            c = capacity
            while c>0 and p<len(passengers) and passengers[p]<= b:
                p+=1
                c-=1
        best = b if c>0 else passengers[p-1]
        passengers = set(passengers)
        while best in passengers:
            best-=1
        return best
        
            
            