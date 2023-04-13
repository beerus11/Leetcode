class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for k,v in enumerate(strs):
            s = "".join(sorted(v))
            m[s].append(v)
        return m.values()
                
            
        
        