class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i,j,k,word):
            if k == len(word):
                return True
            #print(i,j,k)
            if i<0 or j<0 or i>len(board)-1 or j> len(board[0])-1:
                return False
            if board[i][j] == "#":
                return False
            if board[i][j]!=word[k]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            a = search(i+1,j,k+1,word)
            b = search(i,j+1,k+1,word)
            c = search(i-1,j,k+1,word)
            d = search(i,j-1,k+1,word)
            board[i][j] = temp
            return any([a,b,c,d])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i,j,0,word):
                    return True
        return False
        