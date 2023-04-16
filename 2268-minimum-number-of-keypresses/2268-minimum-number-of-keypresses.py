class Solution:
    def minimumKeypresses(self, s: str) -> int:
        m = Counter(s)
        count = 0
        for k,v in enumerate(sorted(m.values(),reverse=True)):
            if k<9:
                count += 1*v
            elif k>=9 and k<18:
                count += 2*v
            else:
                count += 3*v
        return count
            
            
        