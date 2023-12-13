class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        hm_col = defaultdict(defaultdict)
        hm_row = defaultdict(defaultdict)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] not in hm_col[j]:
                    hm_col[j][mat[i][j]]=0
                if mat[i][j] not in hm_row[i]:
                    hm_row[i][mat[i][j]]=0
                    
                hm_col[j][mat[i][j]]+=1
                hm_row[i][mat[i][j]]+=1
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and hm_col[j][1]==1 and hm_row[i][1]==1:
                    count+=1
        return count
        