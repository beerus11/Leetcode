class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = [(startGene,0)]
        seen = set()
        bs = set(bank)
        while q:
            n,s = q.pop(0)
            if n == endGene:
                return s
            for c in "ACGT":
                for i in range(len(n)):
                    nei = n[:i]+c+n[i+1:]
                    if nei not in seen and nei in bs:
                        q.append((nei,s+1))
                        seen.add(nei)
        return -1
            
        