class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hm = Counter(tasks)
        count = 0
        for k,v in hm.items():
            if v==1:
                return -1
            if v%3==0:
                count+=(v//3)
            else:
                count+= (v//3)+1
        return count
                
        
        
        