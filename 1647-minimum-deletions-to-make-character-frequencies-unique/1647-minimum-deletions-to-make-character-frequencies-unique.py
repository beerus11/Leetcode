class Solution:
    def minDeletions(self, s: str) -> int:
        m = Counter(s)
        frequency = [v for k,v in m.items()]
        frequency.sort(reverse=True)
        
        delete_count = 0
        mx_frq_allowed = len(s)
        
        for freq in frequency:
            if freq>mx_frq_allowed:
                delete_count += freq - mx_frq_allowed
                freq = mx_frq_allowed
            mx_frq_allowed = max(0,freq-1)
        
        return delete_count
            
        