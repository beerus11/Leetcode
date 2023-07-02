class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        ss = set()
        for c in s:
            if c in ss:
                count+=1
                ss = set()      
            ss.add(c)
        return count+1
        
        