class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ac,bc = 0,0
        for i in range(1,len(colors)-1):
            if colors[i-1]==colors[i+1]==colors[i]:
                if colors[i]=="A":
                    ac+=1
                else:
                    bc+=1
        return ac>bc
        
        