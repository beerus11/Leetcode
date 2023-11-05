class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count,last_winner,new_winner = 0,-1,-1
        mx = max(arr)
        q = arr[:]
        a,b = q.pop(0),q.pop(0)
        while win_count<k:
            new_winner = -1
            if a==mx or b==mx:
                return mx
            if a>b:
                new_winner=a
                q.append(b)
                b = q.pop(0)
            else:
                new_winner=b
                q.append(a)
                a = q.pop(0)
                
            if last_winner == -1 or new_winner!=last_winner:
                win_count=1
            else:
                win_count+=1
            last_winner = new_winner
        return new_winner
                
        