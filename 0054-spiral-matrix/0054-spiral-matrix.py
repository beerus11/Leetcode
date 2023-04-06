class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        r,c = len(matrix),len(matrix[0])
        up,left,right,down=0,0,c-1,r-1
        
        while len(result) < r*c:
            for col in range(left,right+1):
                result.append(matrix[up][col])
                
            for row in range(up+1,down+1):
                result.append(matrix[row][right])
                
            if up!=down:
                for col in range(right-1,left-1,-1):
                    result.append(matrix[down][col])
            
            if left !=right:
                for row in range(down-1,up,-1):
                    result.append(matrix[row][left])
            left +=1
            right -=1
            up +=1
            down -=1
            
        return result
                
            
            
        