class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"
        trie = {}
        for w in words:
            node = trie
            for l in w:
                node = node.setdefault(l,{})
            node[WORD_KEY]=w
            
        rows,cols = len(board),len(board[0])
        matchedWords = []
        def bt(r,c,parent):
            l = board[r][c]
            cn = parent[l]
            word_match = cn.pop(WORD_KEY,False)
            if word_match:
                matchedWords.append(word_match)
            board[r][c]="#"
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = r + rowOffset, c + colOffset
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                        continue
                if not board[newRow][newCol] in cn:
                    continue
                bt(newRow,newCol,cn)
            board[r][c]=l
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    bt(i,j,trie)
                    
        return matchedWords
                
        