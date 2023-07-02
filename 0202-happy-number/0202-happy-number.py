class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            n=sum(map(lambda x:int(x)**2,list(str(n))))
        return True
        