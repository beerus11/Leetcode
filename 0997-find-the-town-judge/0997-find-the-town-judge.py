class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust==[]:
            return 1
        m = defaultdict(int)
        persons = set()
        non_judges = set()
        mx_trust = 0
        judge = -1
        for item in trust:
            a,b = item
            m[b]+=1
            if m[b]>mx_trust:
                mx_trust =m[b]
                judge=b
            persons.add(a)
            non_judges.add(a)
            persons.add(b)
                  
        if mx_trust!=len(persons)-1 or judge in non_judges:
            return -1
        for k,v in m.items():
            if v==mx_trust and k!=judge:
                return -1
            
        return judge
    
    