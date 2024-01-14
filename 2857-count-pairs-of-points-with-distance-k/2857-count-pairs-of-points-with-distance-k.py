class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = 0
        hm = defaultdict(int)
        for x,y in coordinates:
            for j in range(k+1):
                count+=hm[(x^j,y^(k-j))]
            hm[(x,y)]+=1
        return count
        