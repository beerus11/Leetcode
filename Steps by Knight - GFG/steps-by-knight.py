from collections import deque
class Solution:
    
    #Function to check if cell indexes are within bounds.
    def isValid(self, x, y, N):
        return (x >= 0 and x < N and y >= 0 and y < N)
    
    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        dxy = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        KnightPos[0]-=1
        KnightPos[1]-=1
        TargetPos[0]-=1
        TargetPos[1]-=1
        
        #using boolean list to mark visited cells and currently 
        #marking all the cells as false
        vis = [[False for i in range(N)] for j in range(N)]
        
        #queue for storing visited cells by knight in board and steps taken.
        q = deque()
        #pushing starting position of knight with 0 distance.
        q.append([KnightPos[0], KnightPos[1], 0])
        
        #marking starting cell as visited.
        vis[KnightPos[0]][KnightPos[1]] = True
        
        while(len(q)):
            
            #storing cell indexes and steps of front element and popping them.
            cur = q.popleft()
            x = cur[0]
            y = cur[1]
            steps = cur[2]
            
            #if we reach the required cell, we return true.
            if(x == TargetPos[0] and y == TargetPos[1]):
                return steps
                
            #using loop to reach all the cells that can be reached by knight.
            for i in range(8):
                
                n_x = x + dxy[i][0]
                n_y = y + dxy[i][1]
                
                #if cell indexes are valid and cell is not visited, we push the 
				#indexes in queue with steps and mark cell as visited.
                if(self.isValid(n_x, n_y, N) and vis[n_x][n_y] == False):
                    q.append([n_x, n_y, steps + 1])
                    vis[n_x][n_y] = True
        return -1
        
        
        


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends