class Food:
    def __init__(self, rating, food):
        self.rating = rating
        self.food = food

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating > other.rating
    
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rm = {}
        self.cm = {}
        self.cfm = defaultdict(list)
        for k,v in enumerate(foods):
            self.rm[foods[k]] = ratings[k]
            self.cm[foods[k]] = cuisines[k]
            heapq.heappush(self.cfm[cuisines[k]],Food(ratings[k],v))
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.rm[food] = newRating
        name = self.cm[food]
        heapq.heappush(self.cfm[name],Food(newRating,food))
    
    def highestRated(self, cuisine: str) -> str:
        high_rated = self.cfm[cuisine][0]
        while self.rm[high_rated.food] != high_rated.rating:
            heapq.heappop(self.cfm[cuisine])
            high_rated = self.cfm[cuisine][0]
            
        return high_rated.food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)