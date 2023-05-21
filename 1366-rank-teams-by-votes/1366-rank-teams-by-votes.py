class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        hashMap = {}
        for vote in votes:
            for indx, char in enumerate(vote):
                if(char in hashMap):
                    hashMap[char][indx] += 1
                else:
                    hashMap[char] = [0] * len(vote)
                    hashMap[char][indx] += 1
        
        result = sorted(list(hashMap.keys()))
        result = sorted(result, key = lambda x: hashMap[x], reverse=True)
        
        return "".join(result)
                
            