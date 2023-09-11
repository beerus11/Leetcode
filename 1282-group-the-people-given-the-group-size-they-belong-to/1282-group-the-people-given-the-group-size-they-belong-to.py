class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        m = defaultdict(list)
        ans = []
        for k,i in enumerate(groupSizes):
            if len(m[i])==i:
                ans.append(m[i])
                m[i]= []
            if len(m[i])<i:
                m[i].append(k)
        for k,v in m.items():
            ans.append(v)
        return ans
            
                
            
        