class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        t = 0
        for i in range(len(shift)):
            d,a = shift[i]
            if d==0:
                t+= a*-1
            else:
                t+=a
        t = t % len(s)
        q = deque(list(s))
        q.rotate(t)
        return "".join(q)
        