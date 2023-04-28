class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n=="1":
            return "0"
        l = len(n)
        candidates = set([str(10**l+1),str((10**(l-1)-1))])
        prefix = int(n[:(l+1)//2])
        for i in [-1, 0, 1]:
            candidate = str(prefix + i)
            if len(candidate) < l // 2:
                candidate = '0' * (l // 2 - len(candidate)) + candidate
            print(candidate)
            if l % 2 == 0:
                candidate = candidate + candidate[::-1]
            else:
                candidate = candidate + candidate[:l // 2][::-1]
            if candidate != n:
                candidates.add(candidate)
        candidates.discard(n)
        return str(min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x))))
        