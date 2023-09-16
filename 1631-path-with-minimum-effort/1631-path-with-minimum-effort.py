class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        
        difference_matrix = [[float('inf')]*col for _ in range(row)]
        difference_matrix[0][0] = 0
        
        v = set()
        queue = [(0, 0, 0)]  # difference, x, y
        
        while queue:
            diff, i,j = heapq.heappop(queue)
            v.add((i,j))
            for a, b in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x,y = i+a,j+b
                if 0 <= x < row and 0 <= y < col and (x,y) not in v :
                    current_difference = abs(heights[x][y]-heights[i][j])
                    max_difference = max(current_difference, difference_matrix[i][j])
                    if difference_matrix[x][y] > max_difference:
                        difference_matrix[x][y] = max_difference
                        heapq.heappush(
                            queue, (max_difference, x, y))
        return difference_matrix[-1][-1]
            
                