class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        i,j = 0, len(tokens)-1
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1
                i+=1
            elif i<j and score>0:
                power+=tokens[j]
                score-=1
                j-=1
            else:
                return score
        return score
        