class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([(0,0)])
        self.ss = {(0,0):1}
        self.h = height
        self.w = width
        self.food = food
        self.food_index = 0
        self.movement = {'U':(-1,0),'L':(0,-1),'R':(0,1),'D':(1,0)}
        

    def move(self, direction: str) -> int:
        x,y = self.snake[0]
        nh = (x+self.movement[direction][0],y+self.movement[direction][1])
        a = nh[0]<0 or nh[0]>=self.h
        b = nh[1]<0 or nh[1]>=self.w
        c = nh in self.ss and nh!=self.snake[-1]
        
        if a or b or c:
            return -1
        
        next_food = self.food[self.food_index] if self.food_index <len(self.food) else None
        
        if self.food_index <len(self.food) and next_food[0]==nh[0] and next_food[1]==nh[1]:
            self.food_index+=1
        else:
            tail = self.snake.pop()
            del self.ss[tail]
        self.snake.appendleft(nh)
        self.ss[nh]=1
        return len(self.snake)-1
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)