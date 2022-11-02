class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = [(start,0)]
        seen = {start}
        while q:
            n,steps = q.pop(0)
            if n == end:
                return steps
            for c in "ACGT":
                for i in range(len(n)):
                    nei = n[:i]+c+n[i+1:]
                    if nei not in seen and nei in bank:
                        q.append((nei,steps+1))
                        seen.add(nei)
        return -1
        