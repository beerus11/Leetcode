class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        matched = []
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        def dfs(r,c,parent):
            l = board[r][c]
            n = parent[l]
            
            word_match = n.pop(WORD_KEY,False)
            if word_match:
                matched.append(word_match)
            board[r][c] = "#"
            
            for ro,co in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = r + ro, c + co 
                if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]):
                    continue
                if not board[newRow][newCol] in n:
                    continue
                dfs(newRow,newCol,n)
            board[r][c] = l
            
            if not n:
                parent.pop(l)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie:
                    dfs(r,c,trie)
        return matched