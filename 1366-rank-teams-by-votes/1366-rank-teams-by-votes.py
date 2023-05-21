from functools import cmp_to_key
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        def sort_rank(a,b):
            x,y = a[1],b[1]
            i=0
            while i<len(x):
                if x[i]>y[i]:
                    return -1
                elif x[i]<y[i]:
                    return 1
                i+=1
            return -1 if ord(a[0])<ord(b[0]) else 1
        hashMap = {}
        for vote in votes:
            for indx, char in enumerate(vote):
                if(char in hashMap):
                    hashMap[char][indx] += 1
                else:
                    hashMap[char] = [0] * len(vote)
                    hashMap[char][indx] += 1
        result = sorted(hashMap.items(), key = cmp_to_key(sort_rank))
        result = [r[0] for r in result]
        return "".join(result)
                
            