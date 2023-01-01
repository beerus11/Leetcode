class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = {}
        w_map = {}
        words = s.split()
        
        if len(words)!=len(pattern):
            return False
        
        for i in range(len(words)):
            w = words[i]
            p = pattern[i]
            print(w,p,p_map)
            if p in p_map:
                if p_map[p]!=w:
                    return False
            elif w in w_map:
                return False
            else:
                p_map[p]=w
                w_map[w]=p
        return True
        